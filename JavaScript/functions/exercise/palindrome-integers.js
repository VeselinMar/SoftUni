function palindromeChecker(arrayNums) {
    
    function isNumberPalindrome(num) {
        const numStr = num.toString();
        const reversedNumStr = numStr.split('').reverse().join('');
        return numStr === reversedNumStr;
    }

    arrayNums.forEach(num => {
        const result = isNumberPalindrome(num);
        console.log(`${result ? 'true' : 'false'}`);
    });
}

palindromeChecker([123,323,421,121]);
palindromeChecker([32,2,232,1010]);