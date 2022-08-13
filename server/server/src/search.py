from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin
import pyrebase

from secrets import firebaseConfig
from helper import sanitize

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route('/word/<query>', methods=["GET"])
@cross_origin
def searchWord(query):
  """
    a sanitized query (s_query) should:
    (1) 
  """
  searchRes = db.child("words").order_by_child("word").equal_to(query).get()
  return searchRes, 200