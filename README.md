# Book_Pie :books:

***Book_pie*** is a web application designed to help users to review the books. This app allows user to register and leave a review for the book and rate is as well, unregistered users can search for the books and see the detailed info about them, the app stores data in Postgresql database and it reads data from both database and Google Books API.

## Main Page
The main page displays a selection of suggested books for the user to read, which are chosen at random and change each time the page is reloaded. This data is sourced from the Google Books API.
![](https://github.com/amak-code/Book_Pie/blob/main/static/images/intro-page-book-pie.gif)

## Search Page
On every page of the web application, there's a navigation bar. Users can take advantage of the search form to find books by author and/or title. The search function uses data from the Google Book API response.
If a user clicks on a specific book, the application will first check if the book is in the database. If it is, all relevant data will be retrieved from there. If not, the data will be fetched from the Google Book API
![](https://github.com/amak-code/Book_Pie/blob/main/static/images/search-page-book-pie.gif)
## Map Page
Users can visit the "Find a Bookstore" page, where Google will showcase their location and display all nearby bookstores. By utilizing the Google Maps API, my application not only presents nearby options but also enables users to access further details by clicking on an icon. This includes whether the store is currently open or closed.
![](https://github.com/amak-code/Book_Pie/blob/main/static/images/map-page-book-pie.gif)
## Rating Page
When a user logs in, they can navigate to their personal user page to view the books they have already rated. For new books, users can visit the book page to rate the book and leave a comment below. All data will be stored in a database, and all users will be able to view book reviews and average ratings, which are calculated by taking all ratings for a particular book and computing an averag
![](https://github.com/amak-code/Book_Pie/blob/main/static/images/rating-page-book-pie.gif)
## <a name="Setup"></a>Setup

There are a few things that are needed for this application to run:

You can copy [requirements.txt](/requirements.txt) file which has a list of all that libraries. <br>
You can install them using this command:</br>
```
pip install -r requirements.txt
```

## <a name="TechStack"></a>Tech Stack
- Postgresql
- SQLAlchemy
- Python
- Flask
- Jinja
- HTML
- CSS
- Bootstrap

