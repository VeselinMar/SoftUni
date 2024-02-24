function expenses(fights, helmet, sword, shield, armor) {

    let cost = 0;
    const twelver = helmet + sword + shield + armor
    const sixer = twelver - armor
    
    for (let i = 1; i <= fights; i++) {
        
        if (i % 12 === 0) {
            cost += twelver;
        }

        else if (i % 6 === 0) {
            cost += sixer;
        }

        else if (i % 3 === 0) {
            cost += sword;
        }

        else if (i % 2 === 0) {
            cost += helmet;
        }
    }
    console.log(`Gladiator expenses: ${cost.toFixed(2)} aureus`)
}

expenses(7, 2, 3, 4, 5)
expenses(23, 12.50, 21.50, 40, 200)
