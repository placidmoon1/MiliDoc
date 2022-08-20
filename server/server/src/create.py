from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase

from mySecrets import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint("create", __name__, url_prefix="/create")
CORS(bp)

@bp.route('/definition', methods=["GET", "POST"])
def create_definition():
  if request.method == "POST":  
    word = request.form["word"]
    milDef = request.form["milDef"]
    enDef = request.form["enDef"]
    koDef = request.form["koDef"]
    return "POST REQUST", 200

  return "This is to endpoint to create definitions for MiliDoc", 200
