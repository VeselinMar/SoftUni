function solve(inputString) {
    const words = inputString.split(" ");

    words.forEach(element => {
        const match = element.match(/^#([a-zA-Z]+)$/);
        if (match) {
            const wordWOsymbol = match[1];
            console.log(wordWOsymbol);
        }
    });
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia');
solve('The symbol # is known #variously in English-speaking #regions as the #number sign');