from flask_restful import fields

user_field = {
    'id' : fields.Integer,
    'username' : fields.String,
    'email' : fields.String,
    'uri' : fields.Url('user')
}

songs_field = {
    'id' : fields.Integer,
    'name': fields.String,
    'album id': fields.Integer,
    'uri' : fields.Url('song')
}

albums_field = {
    'id' : fields.Integer,
    'name' : fields.String,
    'uri' : fields.Url('album')

}

artists_field = {
    'id' : fields.Integer,
    'name' : fields.String,
    'uri' : fields.Url('artist')
}