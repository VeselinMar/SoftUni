function solve() {
    const inputNumberElement = document.getElementById('input');
    const resultElement = document.getElementById('result');
    const selectMenuToElement = document.getElementById('selectMenuTo');
    const convertButtonElement = document.querySelector('button');
    
    const binaryOptionElement = selectMenuToElement.querySelector('option');
    binaryOptionElement.value = 'binary';
    binaryOptionElement.textContent = 'Binary';

    const hexaDecimalElement = document.createElement('option');
    hexaDecimalElement.value = 'hexadecimal';
    hexaDecimalElement.textContent = 'Hexadecimal';
    selectMenuToElement.appendChild(hexaDecimalElement);

    const convertors = {
        binary: convertToBinary,
        hexadecimal: convertToHexadecimal,
    }

    convertButtonElement.addEventListener('click', () => {
        const numberValue = Number(inputNumberElement.value)
        resultElement.value = convertors[selectMenuToElement.value](numberValue);
    });

    function convertToBinary(decimal) {
        if (decimal === 0) {
            return '0';
        }

        let binary = '';

        while (decimal > 0) {
            let remainder = decimal % 2;

            binary = remainder + binary;
            decimal = Math.floor(decimal / 2);
        }
        return binary;
    }

    function convertToHexadecimal(decimal) {
        if (decimal === 0) {
            return "0";
        }
        let hexadecimal = "";

        while (decimal > 0) {
            let remainder = decimal % 16;

            let hexDigit = remainder < 10 ? String(remainder) : String.fromCharCode(remainder + 55);

            hexDigit = hexDigit.toUpperCase();

            hexadecimal = hexDigit + hexadecimal;

            decimal = Math.floor(decimal / 16);
        }
        return hexadecimal;
    }
}
