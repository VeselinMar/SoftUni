function solve(inputArray, rotations) {
    let result = inputArray;

    for(let i = 0; i < rotations; i++) {
        element = result.shift();
        result.push(element);
    }

    console.log(result.join(" "));
}

solve([51, 47, 32, 61, 21], 2);
solve([32, 21, 61, 1], 4);
solve([2, 4, 15, 31], 5);