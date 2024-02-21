function printSum(start, end) {
    let result = 0
    let valuesString = ''

    for(let i = start; i <= end; i++) {
        valuesString += i + ' ';
        result += i;
    }
    
    console.log(valuesString)
    console.log(`Sum: ${result}`);
}

printSum(5, 10)
printSum(0,26)
printSum(50, 60)