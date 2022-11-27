const name = document.getElementById('first_name')
const lastname = document.getElementById('last_name')
const password = document.getElementById('password1')
const password2 = document.getElementById('password2')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
    let messages = []
    if (name.value === '' || name.value == null) {
        messages.push('First Name is required')
    }

    if (lastname.value === '' || lastname.value == null) {
        messages.push('Last Name is required')
    }

    if (password.value.length <= 8) {
        messages.push('Password must be longer than 6 charaters')
    }

    if (password.value != password2.value) {
        messages.push('Please make sure that your passwords match')
    }

    if (messages.length > 0) {
        e.preventDefault() // prevent submit
        errorElement.innerText = messages.join(' || ')
    }
})