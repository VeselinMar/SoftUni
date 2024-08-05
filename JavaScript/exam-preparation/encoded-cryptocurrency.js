function encode_crypto(arrayInput) {

    let decoded_crypto = arrayInput.shift();

    for (line of arrayInput) {
        let command = '';
        let parameter = '';
        let replacement = '';
 
        if (line.includes('?')) {
            const [first, second, third] = line.split('?');
            command = first;
            parameter = second;
            replacement = third;
        } else {
            command = line;
        }

        if (command === "TakeEven") {
            decoded_crypto = decoded_crypto.split('').filter((_, index) => index % 2 === 0).join('');
            console.log(decoded_crypto);

    } else if (command === "ChangeAll") {
        decoded_crypto = decoded_crypto.split(parameter).join(replacement);
        console.log(decoded_crypto);

    } else if (command === "Reverse") {
        if (decoded_crypto === parameter) {
            decoded_crypto = decoded_crypto.split('').reverse().join('');
            console.log(decoded_crypto);
        } else if (decoded_crypto.includes(parameter)) {
            const index = decoded_crypto.indexOf(parameter);
            const reversedPart = decoded_crypto.substring(index).split('').reverse().join('');
            decoded_crypto = decoded_crypto.substring(0, index) + reversedPart;
            console.log(decoded_crypto);
        } else {
            console.log('error')
        }
    } else if (command === "Buy") {
        console.log(`The cryptocurrency is: ${decoded_crypto}`);
        break;
    }
}
}

test_data = (["PZDfA2PkAsakhnefZ7aZ", 
"TakeEven",
"TakeEven",
"TakeEven",
"ChangeAll?Z?X",
"ChangeAll?A?R",
"Reverse?PRX",
"Buy"])

test_data_2 = (["z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs", 
"TakeEven",
"Reverse?!nzahc",
"ChangeAll?m?g",
"Reverse?adshk",
"ChangeAll?z?i",
"Buy"])




encode_crypto(test_data);
encode_crypto(test_data_2);
