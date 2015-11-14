from api.models import Songs
from flask_restful import Resource, reqparse, marshal
from constant_vals import songs_field

class SongsListAPI(Resource):

    def __init__(self):
        self.parser =  reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=int, required=True,
                                location='json', help="ID required")
        self.parser.add_argument('name', type=str, required=True,
                                location='json', help="Name required")
        self.parser.add_argument('album', type=str, required=True,
                                 location='json',help="Album required")
        super(SongsListAPI, self).__init__()

    def get(self):
        songs = Songs.query.all()
        try:
            return {"songs" : [marshal(song, songs_field) for song in songs] }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve artists."}, 404


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
        song = Songs.query.filter_by(id=id).first()
        try:
            return {"song" : marshal(song, songs_field) }
        except Exception as e:
            print(e)
            return {"error" : "Failed to retrieve song."}, 404



