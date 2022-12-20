import os
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from jinja2 import StrictUndefined
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# API_KEY = os.environ['GOOGLEBOOK_KEY']

@app.route("/")
def homepage():
    """Return 10 books for the homepage to suggest to the user"""

    url = "https://www.googleapis.com/books/v1/volumes"

    # payload = {'apikey': API_KEY}
    payload = {'q' : 'publishedDate=2022'}

    res = requests.get(url, params=payload)
    print("//////////////////////////////////////////////")
    print(res.url)
    print("//////////////////////////////////////////////")
    data = res.json()
    
    results = data['items']

    return render_template('homepage.html', books = results)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')