
// Function to display hall details in the popup
function showHallDetails(name, price, capacity, chairs, speakers, hallId) {
    document.getElementById('hall-name').textContent = name;
    document.getElementById('hall-price').textContent = price;
    document.getElementById('hall-capacity').textContent = capacity;
    document.getElementById('hall-chairs').textContent = chairs;
    document.getElementById('hall-speakers').textContent = speakers;
    document.getElementById('booking-form').dataset.hallId = hallId; // Set hall ID
    document.getElementById('hall-details-popup').style.display = 'flex';
}

// Function to hide popups
function hidePopup() {
    document.getElementById('hall-details-popup').style.display = 'none';
    document.getElementById('booking-form-popup').style.display = 'none';
}

// Function to show booking form popup
function bookHall() {
    document.getElementById('hall-details-popup').style.display = 'none';
    document.getElementById('booking-form-popup').style.display = 'flex';
}

// Initialize intl-tel-input
document.addEventListener('DOMContentLoaded', function() {
    var input = document.querySelector("#contact");
    var iti = window.intlTelInput(input, {
        initialCountry: "auto",
        separateDialCode: true,
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Set form action
    document.getElementById('booking-form').action = '/submit_booking/';

    // Fetch and set CSRF token
    fetch('/get_csrf_token/')
      .then(response => response.json())
      .then(data => {
        document.getElementById('csrf-token').value = data.csrfToken;
      })
      .catch(error => console.error('Error fetching CSRF token:', error));
  });