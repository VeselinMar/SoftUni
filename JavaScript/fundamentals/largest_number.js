function largest_number(num_1, num_2, num_3) {
    let largest;

    if(num_1 > num_2 && num_1>num_3) {
        largest = num_1
    }
    else if(num_2 > num_1 && num_2 > num_3) {
        largest = num_2
    }
    else if(num_3 > num_1 && num_3 > num_2) {
        largest = num_3
    }
    
    console.log(`The largest number is ${largest}.`)
}

largest_number(5, -3, 16)
largest_number(-3, -5, -22.5)