from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

api = Api(app)
db = SQLAlchemy(app)


#import resources
from .resources import UserListAPI

API_VERSION = Config.API_VERSION
#register resources
api.add_resource(UserListAPI,
                 '/users'.format(version=API_VERSION),
                 endpoint='users', strict_slashes=False)

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Content-Type', 'application/json')
    return response
