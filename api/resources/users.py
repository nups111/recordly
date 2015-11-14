from api.models import Users
from api import db
from flask_restful import Resource, reqparse, marshal
from constant_vals import user_field
from flask import make_response, render_template


class UserListAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser( bundle_errors=True)
        self.parser.add_argument('id', type=int, required=False,
                                location='form', help="ID required")
        self.parser.add_argument('username', type=str, required=True,
                                location='form', help="Username required")
        self.parser.add_argument('password', type=str, required=True,
                                 location='form',help="Password required")
        self.parser.add_argument('email', type=str, required=False,
                                 location='form',help="Email required")
        super(UserListAPI, self).__init__()

    def get(self):
        users = Users.query.all()
        try:
            return {"users" : [marshal(user, user_field) for user in users] }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve users."}, 404

    def post(self):
        args = self.parser.parse_args()
        try:
            user = Users(username=args["username"])
            if args["email"] is not None:
                user.email = args["email"]
                if args["password"] is not None:
                    user.hash_password(args["password"])
                if (self.username_in_db(user)):
                    return {"error":"username already exists"}, 404
                if (self.email_in_db(user)):
                    return {"error":"email id already exists"}, 404
                db.session.add(user)
                db.session.commit()
                headers = {'Content-Type': 'text/html'}
                return make_response(render_template('index.html', user=user),200, headers)
            else:
                user_in_db = Users.query.filter_by(username=user.username).first()
                if user_in_db is not None:
                    if(user_in_db.verify_password(args["password"])):
                        headers = {'Content-Type': 'text/html'}
                        return make_response(render_template('index.html', user=user_in_db),200, headers)
                    else:
                        return {"error":"Invalid username or password"}, 404
        except Exception as e:
            print(e)
            return {"error":"Error creating new user",
                    "msg" : str(e) }, 404


    def username_in_db(self,user):
        user_in_db = Users.query.filter_by(username=user.username).first()
        if user_in_db is not None:
            return True
        return False

    def email_in_db(self,user):
        user_in_db = Users.query.filter_by(username=user.email).first()
        if user_in_db is not None:
            return True
        return False

class UserAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('username', type=str, required=True,
                                location='json', help="Username required")
        self.parser.add_argument('email', type=str, required=True,
                                 location='json',help="Email required")
        super(UserAPI, self).__init__()

    def get(self, id):
        user = Users.query.filter_by(id=id).first()
        try:
            return {"user" : marshal(user, user_field) }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve user."}, 404


    def post(self):
        args = self.parser.parse_args()
        try:
            user = Users(username=args["username"])
            user_in_db = Users.query.filter_by(username=user.username).first()
            pwd_in_db = user_in_db.password
            if(user.verify_password(pwd_in_db)):
                return {"user" : marshal(user, user_field)}, 200
        except Exception as e:
            print(e)
            return {"error":"Error creating new user",
                    "msg" : str(e) }, 404






