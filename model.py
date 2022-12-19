"""Models for book review app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    """A book"""
    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    published_date = db.Column(db.DateTime)
    description = db.Column(db.String)
    poster_path = db.Column(db.String)
    

    reviews = db.relationship("Review", back_populates="book")
    book_genres = db.relationship("BookGenre", back_populates = "book")
    books_to_read = db.relationship("BookToRead", back_populates = "book")

    def __repr__(self):
        return f"<Book book_id={self.book_id} title={self.title}>"



    
class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String)
    user_picture = db.Column(db.String)
    zipcode = db.Column(db.Integer)

    reviews = db.relationship("Review", back_populates="user")
    books_to_read = db.relationship("BookToRead", back_populates = "user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Review(db.Model):
    """A book review."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating = db.Column(db.Integer)
    text_review = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    book = db.relationship("Book", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} score={self.text_review}>"

class BookGenre(db.Model):
    """A book genre."""

    __tablename__ = "bookgenres"

    bookgenre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"))

    book = db.relationship("Book", back_populates="book_genres")
    genre = db.relationship("Genre", back_populates="book_genre")

    def __repr__(self):
        return f"<Book genre bookgenre_id={self.bookgenre_id}>"

class Genre(db.Model):
    """A genre."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre = db.Column(db.String)
    
    book_genre = db.relationship("BookGenre", back_populates="genre")

    def __repr__(self):
        return f"<Genre genre_id={self.genre_id} and genre = {self.genre}>"


class BookToRead(db.Model):
    """A genre."""

    __tablename__ = "books_to_read"

    book_to_read_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    book = db.relationship("Book", back_populates="books_to_read")
    user = db.relationship("User", back_populates="books_to_read")

    def __repr__(self):
        return f"<Genre genre_id={self.genre_id} and genre = {self.genre}>"



def connect_to_db(flask_app, db_uri="postgresql:///book_review", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    """CHANGE IT LATER TO from server import app"""
    from server import app

    connect_to_db(app)
    
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    # app = Flask(__name__)
    
    # db.create_all()
    # test_user = User(email='test2@test.test', password='test')
    # db.session.add(test_user)
    # db.session.commit()
    
    # user = User.query.first()