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
    google_book_id, title, authors, published_date, description, poster_path = (
        book["google_book_id"],
        book["title"],
        book["authors"],
        book["published_date"],
        book["description"],
        book["poster_path"],
    )
    

    db_book = crud.create_book(google_book_id, title, authors, published_date, description, poster_path)
    books_in_db.append(db_book)

model.db.session.add_all(books_in_db)
model.db.session.commit()


# Create 10 users
for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password, nickname='', user_picture='', zipcode=None)
    model.db.session.add(user)


model.db.session.commit()