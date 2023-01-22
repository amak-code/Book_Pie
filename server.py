import os
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
from jinja2 import StrictUndefined
import requests
import crud
import random
import os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
os.system("source secret.sh")
API_KEY = os.environ['GOOGLEMAP_KEY']

LIST_OF_RANDOM_WORDS = ["love", "world", "fashion", "peace", "mindfulness", "sun",
 "modern", "human", "health", "nature", "baby", "detective", "romance", "kid", 
 "animal", "theater", "cook", "bake", "sex", "vacation", "parent", "movie", "history", "english"]

# Homepage methods
@app.route("/")
def homepage():
    """Return 10 books for the homepage to suggest to the user"""

    
    random_word = random.choice(LIST_OF_RANDOM_WORDS)

    url = "https://www.googleapis.com/books/v1/volumes"

    
    payload = {'q' : f'intitle:"{random_word}"', 'orderBy':"newest"}

    res = requests.get(url, params=payload)
    print("//////////////////////////////////////////////")
    print(res.url)
    print("PAYLOAD FOR HOMEPAGE")
    print(payload)
    print("//////////////////////////////////////////////")
    data = res.json()
    
    results = data['items']

    return render_template('homepage.html', books = results)


# Search and show results and details methods
@app.route("/search", methods=["POST"])
def find_books():
    """Search for the books using title and/or author"""

    title = request.form.get('title', '')
    author = request.form.get('author', '')

    # If user didn't type anything
    if title == '' and author == '':
        flash("Please type book's title or author!")
        return redirect("/")

    url = "https://www.googleapis.com/books/v1/volumes"

    search_terms = []
    if title:
        search_terms.append(f"intitle:\"{title}\"")
    if author:
        search_terms.append(f"inauthor:\"{author}\"")
        
    payload = {'q': ' '.join(search_terms)}
   

    res = requests.get(url, params=payload)
    print("//////////////////////////////////////////////")
    print("BOOOKKKK SEARCHHHHH")
    print(res.url)
    print("PAYLOAD FOR SEARCH RESULTS")
    print(payload)
    print("//////////////////////////////////////////////")
    data = res.json()
    if not 'items' in data:
        flash("Sorry! We couldn't find anything.")
        return redirect("/")
    else:
        results = data['items']
        return render_template('search_results.html', books = results)




@app.route("/search/<google_book_id>")
def show_book(google_book_id):
    """Show details of a particular book."""

    db_book = crud.get_book_by_google_id(google_book_id)
    # if book exists in db we fetch it from db

    # if book is not in db we fetch book from google api by it's id
    url = f"https://www.googleapis.com/books/v1/volumes/{google_book_id}"
    res = requests.get(url)
    print("//////////////////////////////////////////////")
    print("BOOOKKKK RESULT")
    print(res.url)
    print("//////////////////////////////////////////////")
    data = res.json()

    already_reviewed = False

    if 'user_id' in session and crud.user_alredy_reviewed_book(session["user_id"], google_book_id):
        already_reviewed = True
        

    return render_template("book-details-page.html", book = data, db_book=db_book, already_reviewed = already_reviewed)

   


# Registration methods
@app.route("/register")
def registration_form():

    return render_template("registration_form.html")

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password, request.form.get("nickname", None), 
            request.form.get("user_picture", None), request.form.get("zipcode", None))
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    

    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect('/')

    else:
        # Log in user by storing the user's id in session
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}!")
        return redirect("/user")
        

@app.route('/logout') 
def log_out():
    """Allow a user to log out."""
    session.clear()
    
    return redirect('/')


# methods for showing reviews on user's page and reviewing the book 

@app.route("/user")
def user_page():
    if session["user_id"]:
        user = crud.get_user_by_id(session["user_id"])
        books = get_suggested_books()
        if user.reviews: 
            reviews = user.reviews
            for review in reviews:
                print(f"SEE HERE:{review.book.authors}")
            # flash(f"Welcome back, {user.email}!", category='info')
            return render_template("user_page.html", user=user, reviews = reviews, books = books)
        else:
           
            # flash(f"Welcome back, {user.email}!")
            return render_template("user_page.html", user=user, books = books)

@app.route("/review", methods=["POST"])
def review_book():
    """Reviewing book and also getting a google_book_id to store this book in db"""
    user_review = request.form.get('review', '')
    google_book_id = request.form.get('googleBookId', '')
    user = crud.get_user_by_id(session["user_id"])
    review = crud.create_review(user_review, google_book_id, user.user_id)

    """Fetching data from google book API using patricular id"""

    url = f"https://www.googleapis.com/books/v1/volumes/{google_book_id}"
    res = requests.get(url)
    data = res.json()
    print('/////////////////////////////')
    print('PRINT AUTHORS')
    print(data['volumeInfo']['authors'])
    if not crud.get_book_by_google_id(google_book_id):
        if 'imageLinks' not in data['volumeInfo']:
            photo = ""
        elif 'thumbnail' not in data['volumeInfo']['imageLinks']:
            photo = ""
        else:
            photo = data['volumeInfo']['imageLinks']['thumbnail']

        if 'averageRating' not in data['volumeInfo']:
            rating = 0
        else:
            rating = data['volumeInfo']['averageRating']
        book = crud.create_book(google_book_id, data['volumeInfo']['title'] , data['volumeInfo']['authors'], photo, rating, number_of_ratings = 0)
        db.session.add(book)
        db.session.commit()
    db.session.add(review)
    db.session.commit()
    
    flash(f"You successfully added a review! ")
    
    return redirect("/user")


# method for rating the book
@app.route("/rating", methods=["POST"])
def rate_the_book():
    value = request.json.get("rating")
    google_book_id = request.json.get("book_id")
    print('/////////////////////////////')
    print('VALUE')
    print(value)

    if not crud.get_book_by_google_id(google_book_id):
        """Fetching data from google book API using patricular id"""

        url = f"https://www.googleapis.com/books/v1/volumes/{google_book_id}"
        res = requests.get(url)
        data = res.json()
        if 'imageLinks' not in data['volumeInfo']:
            photo = ""
        elif 'thumbnail' not in data['volumeInfo']['imageLinks']:
            photo = ""
        else:
            photo = data['volumeInfo']['imageLinks']['thumbnail']

        if 'averageRating' not in data['volumeInfo']:
            rating = 0
        else:
            rating = data['volumeInfo']['averageRating']
        book = crud.create_book(google_book_id, data['volumeInfo']['title'] , 
                data['volumeInfo']['authors'], photo, rating, number_of_ratings = 1)
        db.session.add(book)
        db.session.commit()

    crud.update_avg_rating(google_book_id, value)
    db.session.commit()
    return {
        "success": True, 
        "status": f"Your rating of {value} has been confirmed"}


# method for showing suggested books for user's review

def get_suggested_books():

    random_word = random.choice(LIST_OF_RANDOM_WORDS)
    url = "https://www.googleapis.com/books/v1/volumes"

    payload = {'q' : f'intitle:"{random_word}"', 'maxResults':"40", 'orderBy':"newest"}
    res = requests.get(url, params=payload)
    data = res.json()
    results = data['items']
    filtered_books = []
    for book in results:
        if ('averageRating'in book['volumeInfo']) and (book['volumeInfo']['averageRating']) >= 4.5 :
            filtered_books.append(book)

    return filtered_books
        

# method for rendering Google Map

@app.route("/map")
def view_map():
    """Map-related code."""

    return render_template("map.html", API_KEY=API_KEY)



if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    app.run(host='0.0.0.0')