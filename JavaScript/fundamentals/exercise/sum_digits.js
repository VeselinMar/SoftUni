function sum_digits(number) {
    let result = 0
    // turn number into a string -> iterate through chars -> convert strings to numbers -> increment
    for(const num of String(number)) {
        result += parseInt(num, 10)
    }
    console.log(result)
}

sum_digits(245678)
sum_digits(97561)
sum_digits(543)