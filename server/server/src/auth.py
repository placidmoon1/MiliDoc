import requests

from flask import Blueprint, jsonify, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase

from mySecrets import firebaseConfig
from helper import sanitize

firebase = pyrebase.initialize_app(firebaseConfig)
bp = Blueprint("auth", __name__, url_prefix="/auth")

auth = firebase.auth()
db = firebase.database()
CORS(bp)

default_domain = "@rok.mil"

def check_userToken():
  if (session.get("userToken") is not None):
    userToken = session["userToken"]
    try:
      decoded_token = auth.get_account_info(userToken)
      return (decoded_token["users"][0]["email"])
    except requests.exceptions.HTTPError:
      return "invalid request"
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
    except:
      return jsonify({'error': 'Incorrect username or password'}), 400
    return jsonify(user)
  return jsonify({'error': 'Incorrect username or password'}), 400


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
    try:
      user = auth.sign_in_with_email_and_password(username, password)
      session['userToken'] = user["idToken"]
      return jsonify({'status': 'Good Copy :)'}), 200
    except requests.exceptions.HTTPError:
      return jsonify({'error': 'Incorrect username or password'}), 400


@bp.route('/logout')
def logout():
  check_userToken()
  session.pop('userToken', None)
  return jsonify({'status': 'Logged out successfully:)'}), 200

@bp.route('/getuserinfo')
def getuserinfo():
  userToken = check_userToken()
  if userToken == "invalid request":
    return jsonify({'status': 'Invalid token'}), 400
  return auth.get_account_info(userToken), 200