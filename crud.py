"""CRUD operations."""

from model import db, User, Book, Review, BookGenre, Genre, BookToRead, connect_to_db


def create_user(email, password, nickname, user_picture, zipcode):
    """Create and return a new user."""

    user = User(email=email, 
        password=password, 
        nickname=nickname, 
        user_picture = user_picture, 
        zipcode = zipcode)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()




def create_book(title, author, published_date, description, poster_path):
    """Create and return a new movie."""

    book = Book(
        title=title,
        author = author,
        published_date = published_date,
        description = description,
        poster_path=poster_path)

    return book


def get_books():
    """Return all books."""

    return Book.query.all()


def get_book_by_id(book_id):
    """Return a book by primary key."""

    return Book.query.get(book_id)

def get_book_by_title(title):

    return Book.query.filter(Book.title == title).all()

def get_book_by_author(author):

    return Book.query.filter(Book.author == author).all()



def create_review(rating, text_review, created_date, book_id, user_id):
    """Create and return a new review."""

    review = Review(rating = rating, 
        text_review = text_review,
        created_date = created_date,
        book_id = book_id,
        user_id = user_id)

    return review


def update_rating(rating_id, new_score):
    """ Update a rating given rating_id and the updated score. """
    score = Review.query.get(rating_id)
    score.rating = (score.rating + new_score)/2


def create_bookgenre(book_id, genre_id):

    bookgenre = BookGenre(book_id =book_id,
        genre_id = genre_id)
    
    return bookgenre

def get_all_bookgenres():
    return BookGenre.query.get.all()

def get_bookgenre_by_id(bookgenre_id):

    return BookGenre.query.get(bookgenre_id)


def create_genre(genre):
    
    genre = Genre(genre = genre)
    
    return genre

def get_all_genres():
    return Genre.query.get.all()

def get_genre_by_id(genre_id):

    return BookGenre.query.get(genre_id)

def get_genre_by_genre(genre):

    return Genre.query.filter(Genre.genre == genre).all()



def create_book_to_read(book_id, user_id):

    book_to_read = BookToRead(book_id = book_id,
        user_id = user_id)

    return book_to_read

def get_all_books_to_read(book_to_read_id):

    return BookToRead.query.get.all()

def get_all_books_to_read_by_is(book_to_read_id):

    return BookToRead.query.get(book_to_read_id)




if __name__ == "__main__":
    from server import app

    connect_to_db(app)
