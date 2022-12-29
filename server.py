import os
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
import requests
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ['GOOGLEBOOK_KEY']


# Homepage methods
@app.route("/")
def homepage():
    """Return 10 books for the homepage to suggest to the user"""

    url = "https://www.googleapis.com/books/v1/volumes"

    
    payload = {'q' : 'publishedDate=2022'}

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
@app.route("/search")
def find_books():
    """Search for the books using title and/or author"""

    title = request.args.get('title', '')
    author = request.args.get('author', '')

    url = "https://www.googleapis.com/books/v1/volumes"

    payload = {'q': f"intitle:\"{title}\" inauthor:\"{author}\""}    

    res = requests.get(url, params=payload)
    print("//////////////////////////////////////////////")
    print("BOOOKKKK SEARCHHHHH")
    print(res.url)
    print("PAYLOAD FOR SEARCH RESULATS")
    print(payload)
    print("//////////////////////////////////////////////")
    data = res.json()
    
    results = data['items']
    # for result in results:
    #     del result['volumeInfo']['imageLinks']['smallThumbnail']
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
    print("BOOOKKKK SEARCHHHHH")
    print(res.url)
    print("PAYLOAD FOR SEARCH RESULATS")
    print("//////////////////////////////////////////////")
    data = res.json()
        
        # result = data['items']
        # for result in results:
        #     del result['volumeInfo']['imageLinks']['smallThumbnail']
    
    return render_template("book-details-page.html", book = data, db_book=db_book)
   


# Registration methods
@app.route("/register")
def registration_form():

    return render_template("registration_form.html")

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    nickname = request.form.get("nickname")
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
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        return redirect("/user")
        

@app.route("/user")
def user_page():
    user = crud.get_user_by_email(session["user_email"])
    if user.reviews: 
        reviews = user.reviews
        print('/////////////////////////////')
        print('USER REVIEWS')
        print(f"SEE HERE:{user.reviews}")
        flash(f"Welcome back, {user.email}!")
        return render_template("user_page.html", user=user, reviews = reviews)
    else:
        print('/////////////////////////////')
        print('USER REVIEWS')
        print(f"SEE HERE:{user.reviews}")
        flash(f"Welcome back, {user.email}!")

        return render_template("user_page.html", user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    app.run(host='0.0.0.0')