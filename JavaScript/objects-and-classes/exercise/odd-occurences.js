function solve(wordsString) {
    const wordsArray = wordsString.split(' ');
    const countedWords = {};

    for (let word of wordsArray) {
        if (countedWords[word.toLowerCase()]) {
            countedWords[word.toLowerCase()] ++;
        } else {
            countedWords[word.toLowerCase()] = 1;
        }
    }
    const result = Object.keys(countedWords).filter(word => countedWords[word] % 2 != 0);
    console.log(result.join(' '));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solve('Cake IS SWEET is Soft CAKE sweet Food');