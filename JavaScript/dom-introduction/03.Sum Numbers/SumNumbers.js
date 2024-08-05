function calc() {
    let firstNumber = parseFloat(document.querySelector("#num1").value);
    let secondNumber = parseFloat(document.querySelector("#num2").value);

    let resultField = document.querySelector("#sum");
    resultField.value = firstNumber + secondNumber

}
