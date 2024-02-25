function spice(yield) {
    let days = 0;
    let amount = 0;
    const MIN_YIELD = 100;
    const SPICE_PER_DAY = 10;
    const SPICE_THRESHOLD = 26;

    for (; yield >= MIN_YIELD; yield -= SPICE_PER_DAY) {
        amount += yield;
        days += 1;
        if (amount >= SPICE_THRESHOLD) {
            amount -= SPICE_THRESHOLD;
        } else {
            break;
        }
    }
    
    // Common code outside the loop
    if (amount >= SPICE_THRESHOLD) {
        amount -= SPICE_THRESHOLD;
    }
    console.log(days);
    console.log(amount);
}

spice(111)
spice(450)
