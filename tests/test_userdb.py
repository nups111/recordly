import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import unittest
from tests import DatabaseTestCase
from api import app, db
from api.models import Users

class UserDBTests(DatabaseTestCase):

    def __init__(self, *args, **kwargs):
        super(UserDBTests, self).__init__(*args, **kwargs)

    def setUp(self):
        db.create_all()
        user = Users(username='usertest',
                    email='usertest@gmail.com',
                     password='usertest')
        db.session.add(user)

    def test_user_is_created_in_db(self):
        """Test user is successfuly created and stored
        in the database"""
        #One user in db currently
        self.assertEqual(len(Users.query.all()), 1)
        user = Users(username='nicki',
                    email='nickiminaj@gmail.com',
                    password='nicki123')
        db.session.add(user)
        self.assertEqual(len(Users.query.all()), 2)
        self.assertEqual(user.email, 'nickiminaj@gmail.com')
        self.assertEqual(user.username, 'nicki')
        self.assertEqual(user.password, 'nicki123')

    def test_password_verification(self):
        """Test user's password is registered and
        successfully verified"""
        user = Users.query.filter_by(username="usertest").first()
        user.hash_password('usertest')
        self.assertEqual(user.verify_password('usertest'), True)


if __name__=='__main__':
    unittest.main()
