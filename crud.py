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




def create_book(google_book_id, title, authors, poster_path, rating, number_of_ratings):
    """Create and return a new movie."""

    book = Book(
        google_book_id = google_book_id,
        title=title,
        authors = ", ".join(authors) if authors is not None else "",
        # authors = authors,
        poster_path=poster_path,
        rating = rating,
        number_of_ratings = number_of_ratings
        )

    return book


def get_books():
    """Return all books."""

    return Book.query.all()

def get_recently_added_books():
    """Return recently added books"""

    return Book.query.join(Review).order_by(Review.created_date.desc()).limit(10).distinct().all()

def get_book_by_id(book_id):
    """Return a book by primary key."""

    return Book.query.get(book_id)

def get_book_by_google_id(google_book_id):
    """Return a book by google_book_id."""

    return Book.query.filter(Book.google_book_id == google_book_id).first()

def get_book_by_title(title):

    return Book.query.filter(Book.title == title).all()

def get_book_by_author(author):

    return Book.query.filter(Book.author == author).all()



def create_review(text_review, google_book_id, user_id):
    """Create and return a new review."""

    review = Review( 
        text_review = text_review,
        google_book_id = google_book_id,
        user_id = user_id)

    return review

def get_user_reviews(user_id):
    """Get all the reviews from a particular user"""
    return Review.query.filter(Review.user_id == user_id).all()

def user_alredy_reviewed_book(user_id, google_book_id):
    """Check if a user has a review for a particular book."""
    
    return bool(Review.query.filter((Review.user_id == user_id)&(Review.google_book_id == google_book_id)).first())
    


def get_rating_by_google_id(google_book_id):
    """ Update a rating given rating_id and the updated score. """
    book = Book.query.filter(Book.google_book_id == google_book_id).first()

    return book.rating
    

def update_avg_rating(google_book_id, new_score):
    """Count average rating per book"""
    book = Book.query.filter(Book.google_book_id == google_book_id).first()
    if book.rating == None:
        book.rating = float(new_score)
        book.number_of_ratings = 1
    else:
        book.rating = (book.rating * book.number_of_ratings + int(new_score)) / (book.number_of_ratings + 1)
        book.number_of_ratings += 1

        print(f"/////////  BOOK RATING: {book.rating} ///////////")
    return book.rating

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
