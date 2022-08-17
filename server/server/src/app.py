from flask import Flask, render_template, make_response, url_for, session, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import os
import pyrebase

from mySecrets import firebaseConfig, app_secret_key
from helper import sanitize

app = Flask(__name__)
cors = CORS(app) #NOTE: see https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
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

  
import auth
app.register_blueprint(auth.bp)

import search
app.register_blueprint(search.bp)
  
import create
app.register_blueprint(create.bp)

import check
app.register_blueprint(check.bp)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
