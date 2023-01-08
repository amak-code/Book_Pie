import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb book_review")
os.system("createdb book_review")
# os.system("psql book_review < seed.sql")
model.connect_to_db(server.app)
model.db.create_all()

with open("static/books.json") as f:
    book_data = json.loads(f.read())

books_in_db = []
for book in book_data:
    google_book_id, title, authors, poster_path, rating, number_of_ratings = (
        book["google_book_id"],
        book["title"],
        book["authors"],
        book["poster_path"],
        book["rating"],
        book["number_of_ratings"]
    )
    

    db_book = crud.create_book(google_book_id, title, authors, poster_path, rating, number_of_ratings)
    books_in_db.append(db_book)

model.db.session.add_all(books_in_db)
model.db.session.commit()


# Create 10 users
for n in range(10):
    email = f"user{n}@test.com"  # A unique email!
    password = "test"

    user = crud.create_user(email, password, nickname='', user_picture='', zipcode=None)
    model.db.session.add(user)


model.db.session.commit()

# Create reviews

with open("static/reviews.json") as f:
    review_data = json.loads(f.read())

reviews_in_db = []
for review in review_data:
    text_review, google_book_id, user_id = (
        review["text_review"],
        review["google_book_id"],
        review["user_id"],
        
    )
    

    db_review = crud.create_review(text_review, google_book_id, user_id)
    reviews_in_db.append(db_review)

model.db.session.add_all(reviews_in_db)
model.db.session.commit()