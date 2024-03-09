function charactersInRange(charOne, charTwo) {
    function convertCharToASCII() {
    let charOneValue = charOne.charCodeAt(0);
    let charTwoValue = charTwo.charCodeAt(0);
    return [charOneValue, charTwoValue];
    }

    let asciiValues = convertCharToASCII();

    if (asciiValues[0] < asciiValues[1]) {
    for(let i = asciiValues[0] + 1; i < asciiValues[1]; i++) {
        process.stdout.write(String.fromCharCode(i) + ' ');
    }
} else {
    for(let i = asciiValues[1] + 1; i < asciiValues[0]; i++) {
        process.stdout.write(String.fromCharCode(i) + ' ');
}
}
    console.log();
}

charactersInRange('a', 'd');
charactersInRange('#', ':');
charactersInRange('C', '#');