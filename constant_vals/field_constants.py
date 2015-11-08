from flask_restful import fields

user_field = {
    'id' : fields.Integer,
    'username' : fields.String,
    'email' : fields.String,
    'uri' : fields.Url('users')
}

songs_field = {
    'id' : fields.Integer,
    'name': fields.String,
    'album id': fields.Integer,
    'uri' : fields.Url('songs')
}

albums_field = {
    'id' : fields.Integer,
    'name' : fields.String,
    'uri' : fields.Url('albums')

}

artists_field = {
    'id' : fields.Integer,
    'name' : fields.String,
    'uri' : fields.Url('artists')
}