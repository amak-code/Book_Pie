'use strict';

document.querySelector('.star-rating').addEventListener('change', (event) => {
    event.preventDefault();
    const formInputs = {
              rating: document.getElementById("star-rating-id").value,
              book_id: document.getElementById("star-rating-id").getAttribute('data-google-book-id'),
            };
    
    fetch('/rating', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
        'Content-Type': 'application/json',
        },
    })
        .then((response) => response.json())
        .then((responseJson) => {
        alert(responseJson.status);
        });

    console.log(formInputs);

});