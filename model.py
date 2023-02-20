"""Models for book review app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    """A book"""
    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    google_book_id = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String)
    authors = db.Column(db.String)
    poster_path = db.Column(db.String)
    rating = db.Column(db.Float)
    number_of_ratings = db.Column(db.Integer)

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
    nickname = db.Column(db.String, nullable=True)
    user_picture = db.Column(db.String, nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)

    reviews = db.relationship("Review", back_populates="user")
    books_to_read = db.relationship("BookToRead", back_populates = "user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"
# select distinct books.* from books join reviews by bookes.id=reviews.book_id order by reviews.date desc limit 10

class Review(db.Model):
    """A book review."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text_review = db.Column(db.String)
    created_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    google_book_id = db.Column(db.String, db.ForeignKey("books.google_book_id"))
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



# EXAMPLE DATA ---------------------------------------------------------------

def example_data():
    """Create some sample data for testing."""

    User.query.delete()
    Book.query.delete()
    Review.query.delete()

    # Example Users
    JackT = User(
                nickname='JackT',
                email='JackT@test.com',
                password='test',
                )

    BevM = User(nickname='BevM',
                email='BevM@test.com',
                password='test',)

    PaulE = User(
                nickname='PaulE',
                email='PaulE@test.com',
                password='test',
                )

    # Example Books
    book1 = Book(
        google_book_id = "5CDuO_6LYpgC",
        title = "Struggling with Iowa's Pride",
        authors = "Wilson J. Warren",
        poster_path = "http://books.google.com/books/content?id=5CDuO_6LYpgC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
        rating = 4,
        number_of_ratings = 1
        )

    book2 = Book(
        google_book_id = "_S5dgR5kPAAC",
        title = "The Pride of the Confederate Artillery",
        authors = "Nathaniel Cheairs Hughes",
        poster_path = "http://books.google.com/books/content?id=_S5dgR5kPAAC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
        rating = 3,
        number_of_ratings = 1)


    # Example Reviews  

    review1 = Review(
        text_review = "The book is amazing!!!",
        google_book_id = "_S5dgR5kPAAC",
        user_id = 1
                    )

    review2 = Review(
        text_review = "The book is good!",
        google_book_id = "_S5dgR5kPAAC",
        user_id = 2
    )

    review3 = Review(
        text_review = "I recommended this book to my friend",
        google_book_id = "5CDuO_6LYpgC",
        user_id = 3)

    db.session.add_all([JackT, BevM, PaulE, book1, book2])
    db.session.commit()
    db.session.add_all([review1, review2, review3])
    db.session.commit()


# ----------------------------------------------------------------------------

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
    
