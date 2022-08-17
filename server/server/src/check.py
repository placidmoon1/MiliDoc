from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase, re

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
    #NOTE: split at, but preserve delimiter (tab, newline, space)
    text = re.split('([\t|\n| ])',request.form["text"])    
    l_data = db.child("limitWords").order_by_child("limit_word").get()
    r_data = db.child("restrictedWords").order_by_child("restricted_word").get()

    sanitized = {}
    num_words = 0
    for word_ind in range(len(text)):
      if (text[word_ind] in ["\t", " "]):
        continue
      if (text[word_ind] == "\n"):
        if (num_words != 0): #if there is a previous word, append \n to it
          sanitized[num_words - 1]["original_word"] += "\n"
          sanitized[num_words - 1]["sugg_word"] += "\n"
          continue
    #for each word
      is_limited = 0
      is_restricted = 0
      sugg_word = ''
      for lim_word in l_data.each():
        if lim_word.val()["limit_word"] == text[word_ind]:
          is_limited = 1
          sugg_word = lim_word.val()["sugg_word"]
          break

      for restricted_Word in r_data.each():
        if restricted_Word.val()["restricted_word"] == text[word_ind]:
          is_restricted = 1
          break
      sanitized[num_words] = {
        "original_word": text[word_ind],
        "word_ind": num_words,
        "is_limited": is_limited,
        "is_restricted": is_restricted,
        "sugg_word": sugg_word
      }
      num_words += 1
    return sanitized, 200
  else:
    return "/check/test (POST) splits text input by space, and preserves Korean, English, and numbers", 200