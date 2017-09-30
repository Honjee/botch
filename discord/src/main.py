# import requests
# response = requests.get('https://httpbin.org/ip')
# print('Your IP is {0}'.format(response.json()['origin']))

from flask import Flask
from flask_cors import CORS
from api_calls.oauth import oauth

app = Flask(__name__)
CORS(app)

@app.route('/')
def helloWorld():
    resp = oauth(req="")
    return resp.client_id
