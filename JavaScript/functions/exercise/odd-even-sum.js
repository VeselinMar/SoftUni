function oddEvenSum(number) {
    function oddSum() {
        let sum = 0;
        let numStr = number.toString();

        for (i = 0; i < numStr.length; i++) {
            if (parseInt(numStr[i]) % 2 != 0) {
            sum += parseInt(numStr[i]);
            }
        }

        return sum;
    }

    function evenSum() {
        let sum = 0;
        let numStr = number.toString();

        for (i = 0; i < numStr.length; i++) {
            if (parseInt(numStr[i]) % 2 == 0) {
                sum += parseInt(numStr[i]);
            }
        }

        return sum;
    }
    console.log(`Odd sum = ${oddSum()}, Even sum = ${evenSum()}`)
}

oddEvenSum(1000435);
oddEvenSum(3495892137259234);