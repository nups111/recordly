from flask_restful import Resource
from flask import make_response, render_template


class Index(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200, headers)

class Home(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html'),200, headers)


class SignUp(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('signup.html'),200, headers)

class SignIn(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'),200, headers)
