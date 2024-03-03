function solve(wordsStr, template) {
    const words = wordsStr.split(", ");

    const replacedTemplate = template.replace(/\*+/g, match => {
        const word = words.find(word => word.length === match.length);
        return word || match;
    });

    console.log(replacedTemplate);
}

solve('great', 'softuni is ***** place for learning new programming languages')
solve('great, learning', 'softuni is ***** place for ******** new programming languages')