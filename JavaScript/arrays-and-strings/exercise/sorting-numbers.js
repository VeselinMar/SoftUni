function solve(numbers) {
    let result = [];

    const sortedNumbers = [...numbers];
    sortedNumbers.sort((a, b) => a - b);

    for (let i = 0; i < numbers.length; i++) {
        if (i % 2 === 0){
            let number = sortedNumbers.shift();
            result.push(number);
        } else {
            let number = sortedNumbers.pop();
            result.push(number);
        }
    }
    return(result);
}

solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);