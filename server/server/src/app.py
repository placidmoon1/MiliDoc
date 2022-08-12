from flask import Flask, render_template, make_response, url_for, session, request
from flask_cors import CORS, cross_origin
import os
import time
import pyrebase

from secrets import firebaseConfig, app_secret_key

app = Flask(__name__)
cors = CORS(app)
app.secret_key = app_secret_key
app.config['CORS_HEADERS'] = 'Content-Type'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def index():
  context = {'message':'Hello MiliDoc Server :)'}
  template = render_template('index.html', context=context)
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
