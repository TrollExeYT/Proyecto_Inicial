let errorsDiv = document.getElementById('error-div')

if (errorsDiv.textContent.trim() !== '') {
    let name = document.getElementById('id_name');
    name.classList.add('is-invalid');
}