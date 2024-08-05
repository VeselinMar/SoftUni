function encodeAndDecodeMessages() {
 
    let getText1 = document.getElementsByTagName('textarea')[0];
    let getText2 = document.getElementsByTagName('textarea')[1];
 
    let button = document.querySelector('main :nth-child(1) button');
    let button2 = document.querySelector('main :nth-child(2) button');
 
    let result = [];
 
    button.addEventListener('click', function () {
        let receivedMessage = getText1.value;
        result = [];        //here
        for (const letter of receivedMessage) {
            let newLetter = String.fromCharCode(letter.charCodeAt(0) + 1);
            result.push(newLetter);
        }
        getText1.value = "";
        getText2.value = result.join('');
    })
 
 
 
    button2.addEventListener('click', function () {
        result=[];
        let receivedMessage = getText2.value;
 
        for (const letter of receivedMessage) {
            let newLetter = String.fromCharCode(letter.charCodeAt(0) - 1);
            result.push(newLetter);
        }
 
        // getText2.value = ''
        getText2.value = result.join('');
        result =[];
    })
 
}
