from api import db

def reset_db():
	db.drop_all()
	db.create_all()

if __name__=='__main__':
	reset_db()