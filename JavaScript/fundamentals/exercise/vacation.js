function vacation(people_count, group_type, week_day) {
    let price
    if(group_type === "Students") {
        switch(week_day) {
            case "Friday":
                price = 8.45 * people_count;
                break;
            case "Saturday":
                price = 9.80 * people_count;
                break;
            case "Sunday":
                price = 10.46 * people_count;
                break;
        }
        if(people_count >= 30) {
            price = price * 0.85
        }
    }
    else if(group_type === "Business") {
        switch(week_day) {
            case "Friday":
                price = 10.90 * people_count;
                break;
            case "Saturday":
                price = 15.60 * people_count;
                break;
            case "Sunday":
                price = 16 * people_count;
                break;
        }
        if(people_count >= 100) {
            price = price - ((price / people_count) * 10)
        }
}   
    else if(group_type === "Regular") {
        switch(week_day) {
            case "Friday":
                price = 15 * people_count;
                break;
            case "Saturday":
                price = 20 * people_count;
                break;
            case "Sunday":
                price = 22.50 * people_count;
                break;
    }
    if(people_count >= 10 && people_count <= 20) {
        price = price * 0.95
    }
    }
    console.log(`Total price: ${price.toFixed(2)}`)
}

vacation(30, "Students", "Sunday")
vacation(40, "Regular", "Saturday")
