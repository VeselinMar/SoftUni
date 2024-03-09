function calculateResources(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;

    let height = 0;
    let counter = 1;

    for (let curSize = base; curSize > 0; curSize -= 2) {
        height += increment;

        let totalArea = curSize ** 2;
        let borderArea = totalArea - (curSize - 2) ** 2;
        let stoneArea = totalArea - borderArea;

        if (curSize <= 2) {
            gold = totalArea * increment;
        } else{
            stone += stoneArea * increment;

            if (counter % 5 == 0) {
                lapis += borderArea * increment;
            }else {
                marble += borderArea * increment
            }
        }

        counter += 1;
    }


    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(height)}`)
}

calculateResources(11, 1);
