from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin
import pyrebase

from secrets import firebaseConfig
from helper import sanitize

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint("create", __name__, url_prefix="/create")

@bp.route('/definition', methods=["GET", "POST"])
@cross_origin
def create_definition():
  if request.method == "POST":  
    word = request.form["word"]
    milDef = request.form["milDef"]
    enDef = request.form["enDef"]
    koDef = request.form["koDef"]

  else:
    return "This is to endpoint to create definitions for MiliDoc", 200
