function solve() {
    const outputElement = document.getElementById('output');
    const textAreaElement = document.getElementById('input');
    const text = textAreaElement.value;
    
    const result = text
        .split('.')
        .filter(sentence => !!sentence)
        .reduce((result, sentence, i) => {
        const resultIndex = Math.floor(i / 3);
        if (!result[resultIndex]) {
            result[resultIndex] = [];
        }

        result[resultIndex].push(sentence.trim());

        return result;
    },[])
    .map(sentences => `<p>${sentences.join('\n')}.</p>`)

    outputElement.innerHTML = result;
}