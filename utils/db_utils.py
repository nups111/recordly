from api import db
from api.models import Users, Artists, Songs, Albums
from werkzeug.security import generate_password_hash

def reset_db():
	db.drop_all()
	db.create_all()

def create_users():
	try:
		user1 = Users(username='user1', email='user1@example.com',
						password=generate_password_hash('user1234'))
		user2 = Users(username='user2', email='user2@example.com',
						password=generate_password_hash('user221234'))
		db.session.add(user1)
		db.session.add(user2)
		db.session.commit()
	except Exception as err:
		print("-- user creation failed..")
		print(err)

def create_albums():
	try:
		album1 = Albums(name='album1')
		album2 = Albums(name='album2')
		db.session.add(album1)
		db.session.add(album2)
		db.session.commit()
	except Exception as err:
		print("-- album creation failed..")
		print(err)

def create_songs():
	try:
		song1 = Songs(name='song1')
		song2 = Songs(name='song2')
		db.session.add(song1)
		db.session.add(song2)
		db.session.commit()
	except Exception as err:
		print("-- song creation failed..")
		print(err)

def create_artists():
	try:
		artist1 = Artists(name='artist1')
		artist2 = Artists(name='artist2')
		db.session.add(artist1)
		db.session.add(artist2)
		db.session.commit()
	except Exception as err:
		print("-- artist creation failed..")
		print(err)

if __name__=='__main__':
	reset_db()
	create_users()
	create_albums()
	create_songs()
	create_users()