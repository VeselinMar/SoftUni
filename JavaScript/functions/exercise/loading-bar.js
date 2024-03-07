function loadingBar(percent) {
    let bar = `${percent}%`
    function percentSymbolsCount() {
        const completedSymbols = Math.floor(percent / 10);
        const remainingSymbols = 10 - completedSymbols;
        bar += ' [' + '%'.repeat(completedSymbols) + '.'.repeat(remainingSymbols) + ']';
    }

    if (percent === 100) {
        bar += ' Complete!';
        console.log(bar);
        console.log('[%%%%%%%%%%]')
    }else {
        percentSymbolsCount();
        console.log(bar);
        console.log('Still loading...')
    }
}

loadingBar(30);
loadingBar(50);
loadingBar(100);