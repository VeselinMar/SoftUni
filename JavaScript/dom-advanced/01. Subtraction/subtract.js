function subtract() {
    let num1 = parseFloat(document.querySelector("#firstNumber").value);
    let num2 = parseFloat(document.querySelector("#secondNumber").value);
    
    let resultField = document.querySelector("#result");

    resultField.textContent = num1 - num2
}