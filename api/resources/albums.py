from api.models import Albums
from flask_restful import Resource, reqparse, marshal
from constant_vals import albums_field

class AlbumsListAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('username', type=str, required=True,
                                location='json', help="Username required")
        self.parser.add_argument('email', type=str, required=True,
                                 location='json',help="Email required")
        super(AlbumsListAPI, self).__init__()

    def get(self):
        albums = Albums.query.all()
        try:
            return {"albums" : [marshal(album, albums_field) for album in albums]}
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve users."}, 404

