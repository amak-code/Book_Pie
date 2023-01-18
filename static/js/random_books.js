'use strict';

window.addEventListener('load', (event) => {
    event.preventDefault();

fetch('/random_suggested_books')
  .then((response) => response.text())
  .then((responseJson) => {
    console.log(responseJson)
    showBooks(responseJson.books)
  });

})

function showBooks(books) {
    const container = document.querySelector('#random_book-list');

}