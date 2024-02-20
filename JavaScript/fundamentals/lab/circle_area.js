function circle_area(num) {
    let area;
    if (typeof num != "number") {
        area = `We can not calculate the circle area, because we receive a ${typeof num}.`;
    }
    else {
        area = (3.14159 * num ** 2).toFixed(2)
    }
    console.log(area)
}

circle_area(5)
circle_area('name')