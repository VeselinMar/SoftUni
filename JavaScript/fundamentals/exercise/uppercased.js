function upper(str) {
    let result = ' ';
    let isWordStart = true;

    for (let i = 0; i < str.length; i++) {
        let currentChar = str[i];
    
    if(/\w/.test(currentChar)) {
        result += currentChar.toUpperCase();
        isWordStart = true;
    } else {
        if(isWordStart && i !== str.length - 1) {
            result += ', ';
            isWordStart = false;
        }
    }
    }
    console.log(result.trim())
}

upper('Hi, how are you?')
upper('hello')