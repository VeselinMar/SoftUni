function orders(product, quantity) {
    function calculateWater() {
        return quantity * 1.00;
    }
    function calculateCoffee() {
        return quantity * 1.50;
    }
    function calculateCoke() {
        return quantity * 1.40;
    }
    function calculateSnacks() {
        return quantity * 2.00;
    }

    switch (product) {
        case 'water':
            console.log(`${calculateWater().toFixed(2)}`);
            break;
        case 'coffee':
            console.log(`${calculateCoffee().toFixed(2)}`);
            break;
        case 'coke':
            console.log(`${calculateCoke().toFixed(2)}`);
            break;
        case 'snacks':
            console.log(`${calculateSnacks().toFixed(2)}`);
            break;
    }
}

orders("water", 5);
orders("coffee", 2);