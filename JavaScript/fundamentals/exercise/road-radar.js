function radar(speed, area) {
    let over = 0
    let speed_limit
    let status
    if(area === "motorway") {
        speed_limit = 130
        if(speed > speed_limit) {
            over = speed - speed_limit
        }
    }
    else if(area === "interstate") {
        speed_limit = 90
        if(speed > speed_limit) {
            over = speed - speed_limit
        }
    }
    else if(area === "city") {
        speed_limit = 50
        if(speed > speed_limit) {
            over = speed - speed_limit
        }
    }
    else if(area === "residential") {
        speed_limit = 20
        if(speed > speed_limit) {
            over = speed - speed_limit
        }
    }
    if(over) {
        if(over <= 20) {
            status = "speeding"
        }
        else if(over <= 40) {
            status = "excessive speeding"
        }
        else {
            status = "reckless driving"
        }
        console.log(`The speed is ${over} km/h faster than the allowed speed of ${speed_limit} - ${status}`)
    }
    else {
        console.log(`Driving ${speed} km/h in a ${speed_limit} zone`)
    }
}

radar(40, 'city')
radar(21, 'residential')
radar(120, 'interstate')
radar(200, 'motorway')