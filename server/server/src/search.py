from flask import Blueprint, Flask, render_template, make_response, url_for, session, request, jsonify
from flask_cors import cross_origin, CORS
import pyrebase
import pandas as pd
import ssl
import http, json
from urllib.parse   import urlencode

ssl._create_default_https_context = ssl._create_unverified_context

from mySecrets import firebaseConfig, ko_dict_api_key
from pathlib import Path

cur_path = str(Path(__file__).resolve().parent)
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint("search", __name__, url_prefix="/search")
CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"
cors = CORS(bp, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expose_headers= CORS_EXPOSE_HEADERS.split(","))
@bp.route('/word', methods=["GET"])
def search_word():
  """
    a sanitized query (s_query) should:
    (1) 
  """
  print(request.form)
  query_lang = request.args.get("lang")
  query = request.args.get("query")

  # NOTE: Requires updating indexOn if using order_by_child!!
  df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')
  df_abandon = pd.read_csv(cur_path + '/abandon_words.csv')
  korean = ""
  english = "" #if there is a match in df_forbidden, populate
  abandon = 0 # if query matches df_abandonS, 1
  def1 = ""
  def2 = ""
  forbidden = "" #if there is a match in df_forbidden, populate

  if query_lang == "ko":
    korean = query
    df_forbid_ko = df_forbidden[df_forbidden['단어명'] == query]
    df_abandon = df_abandon[df_abandon['금지어'] == query]
    if not df_forbid_ko.empty:
      english = df_forbid_ko.iloc[0]["영문명"]
      if pd.isna(df_forbid_ko.iloc[0]["금칙어"]):
        forbidden = ""
      else:
        forbidden = df_forbid_ko.iloc[0]["금칙어"]
    if not df_abandon.empty:
      abandon = 1
    
    URL = 'stdict.korean.go.kr'
    #NOTE: verify=false if SSL requests!!!!!!!!!!!
    path = '/api/search.do?' + urlencode({'key': ko_dict_api_key, 'q':query, 'req_type': 'json'}, encoding='utf-8')
    app = Flask(__name__)
    app.logger.info("path", path)
    connection = http.client.HTTPSConnection(URL)
    connection.request("GET", path)
    response = connection.getresponse()
    string = response.read()
    #print("response", string)
    json_obj = json.loads(string)
    #print(json_obj)
    try:
      if len(json_obj["channel"]["item"]) >= 2:
        def1 = json_obj["channel"]["item"][0]["sense"]["definition"]
        def2 = json_obj["channel"]["item"][1]["sense"]["definition"]
      if len(json_obj["channel"]["item"]) == 1:
        def1 = json_obj["channel"]["item"][0]["sense"]["definition"]
    except:
      pass
    
  elif query_lang == "en":
    english = query
    query = query.lower()
    #print(query)
    df_forbid_en = df_forbidden[df_forbidden['영문명'].str.match(query, case=False, na=False)]
    if not df_forbid_en.empty:
      korean = df_forbid_en.iloc[0]["단어명"]
      if pd.isna(df_forbid_en.iloc[0]["금칙어"]):
        forbidden = ""
      else:
        forbidden = df_forbid_en.iloc[0]["금칙어"]
  else:
    return jsonify({'error': 'Invalid language'}), 400
  res = make_response(jsonify({
    "korean": korean,
    "english": english,
    "abandon": abandon,
    "forbidden": forbidden,
    "def1": def1,
    "def2": def2
  }))
  res.headers.add('Access-Control-Allow-Origin', '*')
  res.headers.add('Access-Control-Allow-Credentials', 'true')


  return res, 200