function powerUp(num, pwr) {
    let result = 1;

    for (let i = 0; i < pwr; i++) {
        result *= num;
    }

    console.log(`${result}`);
}

powerUp(2,8);
powerUp(3,4);
