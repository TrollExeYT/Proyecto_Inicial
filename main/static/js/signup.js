let userError = document.getElementById("user-error");
let pass1Error = document.getElementById("pass1-error");
let pass2Error = document.getElementById("pass2-error");

if (userError.textContent.trim() !== '') {
    let username = document.getElementById("username");
    username.classList.add("is-invalid");
}

if (pass1Error.textContent.trim() !== '') {
    let pass1 = document.getElementById("password1");
    pass1.classList.add("is-invalid");
}

if (pass2Error.textContent.trim() !== '') {
    let pass2 = document.getElementById("password2");
    pass2.classList.add("is-invalid");
}