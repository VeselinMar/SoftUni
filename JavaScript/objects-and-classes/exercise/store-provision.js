function solve(stock, delivery) {
    const productsAvailable = {};
    
        for (let i = 0; i < stock.length; i += 2) {
            let nameOfProduct = stock[i];
            let quantityOfProduct = Number(stock[i + 1]);

                productsAvailable[nameOfProduct] = quantityOfProduct;
        }

        for (let i = 0; i < delivery.length; i += 2) {
            let nameOfProduct = delivery[i];
            let quantityOfProduct = Number(delivery[i + 1]);

            if (nameOfProduct in productsAvailable) {
                productsAvailable[nameOfProduct] += quantityOfProduct;
            } else {
                productsAvailable[nameOfProduct] = quantityOfProduct;
            }
        }

    for (product in productsAvailable) {
        console.log(`${product} -> ${productsAvailable[product]}`);
    }
}

solve([
    'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
    'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ]);
