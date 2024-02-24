function sumDigits(number) {
    let result = 0
    // turn number into a string -> iterate through chars -> convert strings to numbers -> increment
    for(const num of String(number)) {
        result += parseInt(num, 10)
    }
    console.log(result)
}

sumDigits(245678)
sumDigits(97561)
sumDigits(543)