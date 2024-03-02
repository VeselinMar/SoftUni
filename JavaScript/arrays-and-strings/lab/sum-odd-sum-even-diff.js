function difference(inputArr) {
    let sumEven = 0;
    let sumOdd = 0;

    for (i = 0; i < inputArr.length; i++) {
        if (inputArr[i] % 2 === 0) {
            sumEven += inputArr[i];
        } else {
            sumOdd += inputArr[i]
        }
    }
    console.log(sumEven - sumOdd)
}

difference([1,2,3,4,5,6]);
difference([3,5,7,9]);
difference([2,4,6,8,10]);