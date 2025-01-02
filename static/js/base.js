function alertButton() {
    alert("Welcome! Thank you for visiting!");
}

/* javascript for list */ 

// Set the authentication state based on Django's context
function handleBookNow(bikeName) {
    if (isAuthenticated === 'true') {
        openModal(bikeName);
    } else {
        openAuthModal(); // Show authentication modal if user is not authenticated
    }
}

function openModal(bikeName) {
    document.getElementById("bookingMessage").textContent = `You are about to book: ${bikeName}`;
    document.getElementById("bookingModal").style.display = "block";
}

function closeModal() {
    document.getElementById("bookingModal").style.display = "none";
}

function confirmBooking() {
    alert(`Your booking for ${document.getElementById("bookingMessage").textContent} has been confirmed!`);
    closeModal(); // Close the modal after confirmation
}

function openAuthModal() {
    document.getElementById("authModal").style.display = "block";
}

function closeAuthModal() {
    document.getElementById("authModal").style.display = "none";
}

function redirectToSignIn() {
    window.location.href = "{% url 'signIn' %}"; // Redirect to sign-in page
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    if (event.target === document.getElementById("bookingModal")) {
        closeModal();
    } else if (event.target === document.getElementById("authModal")) {
        closeAuthModal();
    } else if (event.target === document.getElementById("actionModal")) {
        closeActionModal();
    }
}




/* RETRIEVE/READ search */

function filterTable(tableId, searchInputId) {
    let input = document.getElementById(searchInputId);
    let filter = input.value.toLowerCase(); // Get the search input value and convert it to lowercase
    let table = document.getElementById(tableId);
    let tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) { // Start from 1 to skip the table header
        let td = tr[i].getElementsByTagName("td");
        
        // Check if the user name (second column, index 1) matches the search input
        if (td[1]) { // td[1] is the user name column
            let txtValue = td[1].textContent || td[1].innerText; // Get the user name
            if (txtValue.toLowerCase().indexOf(filter) > -1) {
                tr[i].style.display = ""; // Show the row if there’s a match
            } else {
                tr[i].style.display = "none"; // Hide the row if no match
            }
        }
    }
}


    // Variables
    let pricePerDay = 0; // Initial price per day is set to 0
    const bikeSelect = document.getElementById('bike');
    const daysBookedInput = document.getElementById('days_booked');
    const totalPriceLabel = document.getElementById('totalPrice');

    // Function to update total price based on selected bike and number of days
    function updateTotalPrice() {
        const daysBooked = parseInt(daysBookedInput.value, 10) || 1; // Default to 1 if invalid
        const totalPrice = (daysBooked * pricePerDay).toFixed(2); // Calculate total price
        totalPriceLabel.textContent = totalPrice; // Update the total price displayed
    }

    // Event listener for bike selection change
    bikeSelect.addEventListener('change', function() {
        const selectedOption = bikeSelect.options[bikeSelect.selectedIndex]; // Get the selected option
        pricePerDay = parseFloat(selectedOption.getAttribute('data-price')) || 0; // Get price from data attribute
        updateTotalPrice(); // Update total price whenever a bike is selected
    });

    // Event listener for days booked input change
    daysBookedInput.addEventListener('input', updateTotalPrice); // Update total price on days input change

    // Initialize total price on page load if bike is pre-selected (in case of editing)
    if (bikeSelect.value) {
        const selectedOption = bikeSelect.options[bikeSelect.selectedIndex];
        pricePerDay = parseFloat(selectedOption.getAttribute('data-price')) || 0;
        updateTotalPrice(); // Set the initial total price when the page loads
    }