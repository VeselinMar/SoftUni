function factorialDivision(firstNum, secondNum) {
    function firstFactorial(num) {
        if (num === 0 || num === 1) {
            return 1;
        } else {
            return num * firstFactorial(num - 1);
        }
    }

    function secondFactorial(num) {
        if (num === 0 || num === 1) {
            return 1;
        } else {
            return num * secondFactorial(num - 1);
        }
    }

    console.log(`${(firstFactorial(firstNum) / secondFactorial(secondNum)).toFixed(2)}`);
}

factorialDivision(5, 2);
factorialDivision(6, 2);