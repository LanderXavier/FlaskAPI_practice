// frontend/js/register.js
$(document).ready(function() {
    $('#register-form').submit(function(e) {
      e.preventDefault(); // Prevent the default form submission
  
      const username = $('#username').val();
      const email = $('#email').val();
      const password = $('#password').val();
      const confirmPassword = $('#confirmPassword').val();
  
      // Simple client-side validation
      if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
      }
  
      // Make an AJAX POST request to the API
      $.ajax({
        url: 'http://127.0.0.1:5000/api/auth/register', // Adjust to your API endpoint
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ username, email, password }),
        success: function(response) {
          if (response.message == 'User created') {
            // Redirect to login page or show a success message
            alert("Registration successful! Please log in.");
            window.location.href = "login.html";
          } else {
            alert("Error: " + response.message);
          }
        },
        error: function(error) {
          console.error("Error during registration:", error);
          alert("An error occurred. Please try again. "  + error);
        }
      });
    });
  });
  