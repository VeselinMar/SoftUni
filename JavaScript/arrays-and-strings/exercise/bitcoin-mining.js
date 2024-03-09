function bitcoinMining(shiftArray) {
    const goldPerGram = 67.51;
    const bitcoinPerCoin = 11949.16;
    const lossPercentage = 0.3;
    let money = 0;
    let day = 0;
    let count = 0;

    for (const element of shiftArray) {
        count += 1;
        if (count % 3 === 0) {     
            money += (element * (1 - lossPercentage)) * goldPerGram;
        } else {
            money += element * goldPerGram;
        }
        if (! day && money >= bitcoinPerCoin) {
            day = count
        }
    }

    let bitcoinsBought = Math.floor(money / bitcoinPerCoin);
    console.log(`Bought bitcoins: ${(bitcoinsBought).toFixed(0)}`);
    if (day) {
        console.log(`Day of the first purchased bitcoin: ${day}`);
    }
    console.log(`Left money: ${(money - (bitcoinsBought * bitcoinPerCoin)).toFixed(2)} lv.`)
}

bitcoinMining([100, 200, 300]);
bitcoinMining([50, 100]);
bitcoinMining([3124.15, 504.212, 2511.124]);