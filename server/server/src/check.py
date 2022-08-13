from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase

from mySecrets import firebaseConfig
from helper import sanitize

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint("check", __name__, url_prefix="/check")
CORS(bp)

@bp.route('/text', methods=["GET", "POST"])
def check_text():
  """
    a sanitized query (s_query) should:
    (1) 
  """
  if request.method == "POST":
    text = request.form["text"].split(' ')
    sanitized = []
    for word in text:
      sanitized.append(sanitize(word, ""))
    return sanitized, 200
  else:
    return "/check/test (POST) splits text input by space, and preserves Korean, English, and numbers", 200