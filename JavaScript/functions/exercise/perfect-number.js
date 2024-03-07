function perfectNumberChecker(number) {
    if (number <= 1) {
        console.log("It's not so perfect.");
        return;
    }

    let sum = 1;

    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            sum += i;
            if (i !== number / i) {
                sum += number / i;
            }
        }
    }

    if (number === sum) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");
    }
}

perfectNumberChecker(6);
perfectNumberChecker(28);
perfectNumberChecker(1236498);