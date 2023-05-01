from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data
from flask import session
import crud
import os
import bcrypt

class FlaskTests(TestCase):
    """Flask tests that use the database."""
    # tests for DataBase
    def hashPw(pw):
        hash_password = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        return hash_password.decode('utf8')

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        # os.system("dropdb testdb")
        # os.system("createdb testdb")
        connect_to_db(app, db_uri="postgresql:///testdb")
        db.drop_all()
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.remove()
        db.engine.dispose()

    
    def test_get_user_by_email(self):
        user = crud.get_user_by_email('JackT@test.com')
        assert('JackT@test.com') == (user.email)

    
    def test_get_book_by_google_id(self):
        book = crud.get_book_by_google_id("_S5dgR5kPAAC")
        assert('The Pride of the Confederate Artillery') == book.title


    def test_does_user_reviewed_book(self):
        bool = crud.user_alredy_reviewed_book('3', '5CDuO_6LYpgC')
        assert(bool) == True

    def test_get_rating_by_google_id(self):
        rating = crud.get_rating_by_google_id('5CDuO_6LYpgC')
        assert(4) == rating

    # ------------------------------------------------------------------
    # tests for pages and sign in/up processes

    def test_welcome_page(self):
        result = self.client.get('/')
        self.assertIn(b'<h3>Thinking what to read next?</h3>',
                    result.data)


    def test_login(self):
        result = self.client.post("/login",
                                  data={"email": "JackT@test.com", "password": "test"},
                                  follow_redirects=True)
        
        self.assertIn(b"Welcome back, JackT@test.com!", result.data)


    def test_log_in_page(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<form action="/login" method="POST">', result.data)


    def test_register_user_success(self):
        # Create a new user with unique email
        form = {
            'email': '123@test.com',
            'password': '123'
        }
        
        response = self.client.post('/users', data=form)
        self.assertEqual(response.status_code, 302) # Successful redirect
        self.assertEqual(response.location, 'http://localhost/') # Redirect to home page
        response = self.client.get(response.location)
        self.assertIn(b'Account created! Please log in.', response.data) # Success message
        


    def test_search_results(self):
        form = {
            'title':'Paradise',
            'author':'John'
        }
        
        response = self.client.post('/search', data = form)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Paradise Lost', response.data)
        
   

   

    

  


   


# ----------------------------------------------------------------------------

if __name__ == "__main__":
    import unittest
    unittest.main()