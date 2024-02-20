function same_numbers(number) {
    let result = 0
    let same = true
    let last = 'a'

    for(const num of String(number)) {
        result += parseInt(num, 10)
        if(last !== 'a' && last !== num) {
            same = false
        }
        last = num
    }
    console.log(same)
    console.log(result)
}
    
same_numbers(2222222)
same_numbers(1234)