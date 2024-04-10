function validate() {
    const inputField = document.getElementById('email');
    const emailRegex = /[a-z]+@[a-z]+\.[a-z]+/;

    inputField.addEventListener('change', function() {
        if (!emailRegex.test(inputField.value)) {
            inputField.classList.add('error');
        } else {
            inputField.classList.remove('error');
        }
    });
}