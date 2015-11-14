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
            return {"error" : "Failed to retrieve artists."}, 404

class ArtistAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('name', type=str, required=True,
                                location='json', help="Name required")
        self.parser.add_argument('album', type=str, required=True,
                                 location='json',help="Album required")
        super(ArtistAPI, self).__init__()

    def get(self, id):
        artist = Artists.query.filter_by(id=id).first()
        try:
            return {"artist" : marshal(artist, artists_field) }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve artist."}, 404
