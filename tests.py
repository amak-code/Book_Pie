from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data
from flask import session
import crud



class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        connect_to_db(app, db_uri="postgresql:///testdb")
        db.create_all()
        example_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_login(self):
        result = self.client.post("/login",
                                  data={"email": "JackT@test.com", "password": "test"},
                                  follow_redirects=True)
        self.assertIn(b"Welcome back, JackT@test.com!", result.data)

    def test_get_user_by_email(self):
        user = crud.get_user_by_email('JackT@test.com')
        assert('JackT@test.com','test', 'JackT') == (user.email,
        user.password,user.nickname)

    
    def test_get_book_by_google_id(self):
        book = crud.get_book_by_google_id("_S5dgR5kPAAC")
        assert('The Pride of the Confederate Artillery') == book.title


    def test_does_user_reviewed_book(self):
        bool = crud.user_alredy_reviewed_book('3', '5CDuO_6LYpgC')
        assert(bool) == True

    def test_get_rating_by_google_id(self):
        rating = crud.get_rating_by_google_id('5CDuO_6LYpgC')
        assert(4) == rating



# ----------------------------------------------------------------------------

if __name__ == "__main__":
    import unittest
    unittest.main()