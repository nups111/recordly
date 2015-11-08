from api.models import Users
from flask_restful import Resource, reqparse, fields, marshal

user_field = {
    'id' : fields.Integer,
    'username' : fields.String,
    'email' : fields.String,
    'uri' : fields.Url('users')
}

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
        print(type(users))
        try:
            for user in users:
                print(marshal(user, user_field))
            return {"users" : [marshal(user, user_field) for user in users] }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve users."}, 404