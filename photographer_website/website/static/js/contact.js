const submitBtn = document.getElementById('submit-btn');

// Add a click event listener to the submit button
submitBtn.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the input values
    const name = document.getElementById('name_input').value;
    const email = document.getElementById('email_input').value;
    const phone = document.getElementById('phone_input').value;
    const message = document.getElementById('msg_text').value;

    var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

    // Create an object with the form data
    const formData = {
        name: name,
        email: email,
        phone: phone,
        message: message
    };

    // Send a POST request to /contact
    fetch('/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(formData)
    })
        .then(response => {
            if (response.ok) {
                // Handle the success response here
                document.getElementById('name_input').value = '';
                document.getElementById('email_input').value = '';
                document.getElementById('phone_input').value = '';
                document.getElementById('msg_text').value = '';

                console.log('Message sent successfully!');
            } else {
                // Handle the error response here
                console.error('Error sending message.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
