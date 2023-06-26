function updateContactForm() {
    const contactForm = document.getElementsByClassName('contact_form')[0]
    const contactFormWrapper = document.getElementsByClassName('form_wrapper')[0]

    contactForm.addEventListener('submit', function () {
        contactFormWrapper.style.display = 'none'
    })
}

updateContactForm()