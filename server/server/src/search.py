from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase

from mySecrets import firebaseConfig
from helper import sanitize

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint("search", __name__, url_prefix="/search")
CORS(bp)

@bp.route('/word/<query>')
def search_word(query):
  """
    a sanitized query (s_query) should:
    (1) 
  """
  # NOTE: Requires updating indexOn if using order_by_child!!
  searchRes = db.child("words").order_by_child('word').equal_to(query).get()
  if searchRes.val() == []:
    return "empty TT", 200
  return searchRes.val(), 200