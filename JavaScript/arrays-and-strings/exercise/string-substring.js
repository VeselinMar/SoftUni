function solve(word, text) {
    const textWords = text.split(" ");

    let wordFound = false;

    textWords.forEach (element => {
        const match = element.match(new RegExp(`^${word}`, 'i'));
        if (match) {
            console.log(word);
            wordFound = true;
        } 
    });

    if (!wordFound) {
        console.log(`${word} not found!`);
    }
}

solve('javascript', 'JavaScript is the best programming language');
solve('python', 'JavaScript is the best programming language');
