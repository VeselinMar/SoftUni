function smallestOfThree(numOne, numTwo, numThree) {

    let smallestOfTwo = function() {
        if (numOne < numTwo) {
            return numOne;
        } else {
            return numTwo;
        }
    }

    if (smallestOfTwo() < numThree) {
        console.log(smallestOfTwo())
    } else {
        console.log(numThree);
    }
}

smallestOfThree(2, 5, 3);
smallestOfThree(600, 342, 123);
smallestOfThree(25, 21, 4);
smallestOfThree(2, 2, 2);
