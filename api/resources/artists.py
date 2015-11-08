from api.models import Artists
from flask_restful import Resource, reqparse, marshal
from constant_vals import artists_field

class ArtistsListAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('name', type=str, required=True,
                                 location='json',help="Name required")
        super(ArtistsListAPI, self).__init__()

    def get(self):
        artists = Artists.query.all()
        try:
            return {"artists" : [marshal(artist, artists_field) for artist in artists] }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve users."}, 404

