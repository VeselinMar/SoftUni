function math(num_1, num_2, operator) {
    let result;

    switch(operator) {
        case '+':
            result = num_1 + num_2;
            break;
        case '-':
            result = num_1 - num_2;
            break;
        case '*':
            result = num_1 * num_2;
            break;
        case '/':
            result = num_1 / num_2;
            break;
        case '%':
            result = num_1 % num_2;
            break;
        case '**':
            result = num_1 ** num_2;
            break;
    }
    console.log(result)
}

math(2,2,'+')
math(5,2,'**')
math(10,5,'/')
math(120,10,'%')