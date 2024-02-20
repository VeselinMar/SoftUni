function cooking(number, first, second, third, fourth, fifth) {
    let num = parseInt(number, 10)
    for (let i = 1; i < arguments.length; i++) {
        arg = arguments[i]
        switch (arg) {
            case "chop":
                num /= 2;
                break;
            case "dice":
                num = Math.sqrt(num);
                break;
            case "spice":
                num += 1;
                break;
            case "bake":
                num *= 3;
                break;
            case "fillet":
                num -= num * 0.2;
                break;
        }
        console.log(num)

    }
}

cooking('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet')