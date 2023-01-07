'use strict';

// var e = document.getElementById("star-rating-id");

// function onChange() {
//   var rating = e.value;
  
//   var book_id = el.getAttribute('data-google-book-id');
//   console.log(rating, book_id);
// }
// e.onchange = onChange;
// onChange();

// document.querySelector('#order-form').addEventListener('submit', (evt) => {
//     evt.preventDefault();
  
//     const formInputs = {
//       type: document.querySelector('#type-field').value,
//       amount: document.querySelector('#amount-field').value,
//     };
  
//     fetch('/new-order', {
//       method: 'POST',
//       body: JSON.stringify(formInputs),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//       .then((response) => response.json())
//       .then((responseJson) => {
//         alert(responseJson.status);
//       });
//   });



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