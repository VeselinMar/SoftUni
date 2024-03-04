function reverse(n, inputArr) {
    let arr = inputArr.slice(0, n);

    const reversed_array = arr.reverse();

    console.log(reversed_array.join(' '))
}

reverse(3, [10, 20, 30, 40, 50]);
reverse(4, [-1, 20, 99, 5]);
reverse(2, [66, 43, 75, 89, 47]);
