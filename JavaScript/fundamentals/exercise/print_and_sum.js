function print_sum(start, end) {
    let result = 0
    let valuesString = ''

    for(let i = start; i <= end; i++) {
        valuesString += i + ' ';
        result += i;
    }
    
    console.log(valuesString)
    console.log(`Sum: ${result}`);
}

print_sum(5, 10)
print_sum(0,26)
print_sum(50, 60)