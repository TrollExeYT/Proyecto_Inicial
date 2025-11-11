let errorsDiv = document.getElementById('error-div')

if (errorsDiv.textContent.trim() !== '') {
    let username = document.getElementById('username');
    let password = document.getElementById('password');
    username.classList.add('is-invalid');
    password.classList.add('is-invalid');
}

