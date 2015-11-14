from api.models import Users
from flask_restful import Resource, reqparse, marshal
from constant_vals import user_field

class UserListAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('username', type=str, required=True,
                                location='json', help="Username required")
        self.parser.add_argument('email', type=str, required=True,
                                 location='json',help="Email required")
        super(UserListAPI, self).__init__()

    def get(self):
        users = Users.query.all()
        try:
            return {"users" : [marshal(user, user_field) for user in users] }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve users."}, 404

class SongAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('name', type=str, required=True,
                                location='json', help="Name required")
        self.parser.add_argument('album', type=str, required=True,
                                 location='json',help="Album required")
        super(SongAPI, self).__init__()

    def get(self, id):
        user = Users.query.filter_by(id=id).first()
        try:
            return {"user" : marshal(user, user_field) }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve user."}, 404



