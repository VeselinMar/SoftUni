function fruit(fruit, grams, price_per_kg) {
    let price = (grams / 1000) * price_per_kg

    console.log(`I need $${price.toFixed(2)} to buy ${(grams / 1000).toFixed(2)} kilograms ${fruit}.`)
}

fruit('orange', 2500, 1.80)
fruit('apple', 1563, 2.35)