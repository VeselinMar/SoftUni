function passwordValidator(password) {

    let lengthIsValid = () => {
        return password.length >= 6 && password.length <= 10;
    }

    let symbolsContainLettersAndDigits = () => {
        return /^[a-zA-Z0-9]+$/.test(password);;
    }

    let containsAtLeastTwoDigits = () => {
        return (password.match(/\d/g) || []).length >= 2;
    }

    if (lengthIsValid() && symbolsContainLettersAndDigits() && containsAtLeastTwoDigits()) {
        console.log("Password is valid");
    } else {
        if (!lengthIsValid()) {
            console.log("Password must be between 6 and 10 characters");
        }
        if (!symbolsContainLettersAndDigits()) {
            console.log("Password must consist only of letters and digits");
        }
        if (!containsAtLeastTwoDigits()) {
            console.log("Password must have at least 2 digits");
        }
    }
}

passwordValidator('logIn');
passwordValidator('MyPass123');
passwordValidator('Pa$s$s');