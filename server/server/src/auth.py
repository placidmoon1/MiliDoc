import requests

from flask import Blueprint, jsonify, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase

from mySecrets import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
bp = Blueprint("auth", __name__, url_prefix="/auth")

auth = firebase.auth()
db = firebase.database()
CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"
cors = CORS(bp, allow_headers=CORS_ALLOW_HEADERS.split(","), supports_credentials = True)

default_domain = "@rok.mil"

def check_uid(option):
  if (session.get("uid") is not None):
    print(session.get("uid"))
    uid = session["uid"]
    try:
      decoded_token = auth.get_account_info(uid)
    except requests.exceptions.HTTPError:
      return "invalid request"
    if option == "email":
      return (decoded_token["users"][0]["email"])
    elif option == "token":
      return uid

        
  return "invalid request"

@bp.route("/register", methods=("GET", "POST"))
def register():
  """
  Register a new user 
  """
  if request.method == "POST":
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    #print ('data from client:', request)
    username = request.form["username"]
    password = request.form["password"]
    secret_status = request.form["secret_status"]
    try:
      user = auth.create_user_with_email_and_password(username, password)
      res = make_response('register success, inserting cookie')
      res.headers.add('Access-Control-Allow-Credentials', 'true')
      res.set_cookie("uid", user["idToken"], samesite='None', secure=True)
      return user, 200
    except:
      return jsonify({'error': 'Invalid request type'}), 400
  return jsonify({'error': 'Invalid request type'}), 400

@cross_origin()
@bp.route("/login", methods=("GET", "POST"))
def login():
  """
  Login a new user 
  """
  if request.method == "POST":
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    #print ('data from client:', request)
    username = request.form["username"]
    password = request.form["password"]
    print("http origin", request.environ.get('HTTP_ORIGIN', '*'))

    try:
      user = auth.sign_in_with_email_and_password(username, password)
      res = make_response('login success, good copy')
      res.headers.add('Access-Control-Allow-Origin', request.environ.get('HTTP_ORIGIN', '*'))
      res.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS, GET');
      res.headers.add('Access-Control-Allow-Credentials', 'true')
      res.headers.add('Access-Control-Allow-Headers', 'access-control-allow-origin,content-type');
      res.set_cookie("uid", user["idToken"])
      return res, 200
    except requests.exceptions.HTTPError:
      return jsonify({'error': 'Incorrect username or password'}), 400


@bp.route('/logout')
def logout():
  check_uid("token")
  session.pop('uid', None)
  return jsonify({'status': 'Logged out successfully:)'}), 200

@bp.route('/user/getemail')
def getuserinfo():
  #print(request.headers)
  #print("http origin", request.environ.get('HTTP_ORIGIN', '*'))
  print('cookies', request.cookies.get('uid'))
  if 'uid' not in request.cookies:
    return jsonify({'status': 'Invalid token'}), 400
  res = make_response(auth.get_account_info(request.cookies.get("uid"))["users"][0]["email"])
  res.headers.add('Access-Control-Allow-Origin', request.environ.get('HTTP_ORIGIN', '*'))
  res.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS, GET');
  res.headers.add('Access-Control-Allow-Credentials', 'true')
  res.headers.add('Access-Control-Allow-Headers', 'access-control-allow-origin,content-type');

  return res, 200