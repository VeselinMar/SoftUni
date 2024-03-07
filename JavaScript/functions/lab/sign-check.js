function signCheck(numOne, numTwo, numThree) {
    let result = '';

    function oneTimesTwo() {
        return numOne * numTwo;
    }
    
    if (oneTimesTwo() * numThree > 0) {
        result = 'Positive';
    } else {
        result = 'Negative';
    }
    console.log(result)
}

signCheck(5, 12, -15);
signCheck(-6, -12, 14);
signCheck(-1, -2, -3);
