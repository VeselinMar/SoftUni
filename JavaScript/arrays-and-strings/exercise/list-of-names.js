function solve(names) {
    names
        .sort((a, b) => {
            if (a.toLowerCase() > b.toLowerCase()) {
                return 1;
            } else if (a.toLowerCase() < b.toLowerCase()) {
                return -1;
            } else {
                return 0;
            }
        } )
        .forEach((name, index) => console.log(`${index + 1}.${name}`));
}

solve(["John", "bob", "Christina", "Ema"])