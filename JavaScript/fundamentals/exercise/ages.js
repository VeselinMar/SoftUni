function ages(age) {
    let age_group
    if(typeof age != "number" || age < 0) {
        age_group = "out of bounds"
    }
    else {
        if(age <= 2) {
            age_group = "baby"
        }
        else if(age <= 13) {
            age_group = "child"
        }
        else if(age <= 19) {
            age_group = "teenager"
        }
        else if(age <= 65) {
            age_group = "adult"
        }
        else {
            age_group = "elder"
        }
    }
    console.log(age_group)
}

ages(20)
ages(1)
ages(100)
ages(-1)    