def shop_from_grocery_list(budget, grocery_list, *args):
    bought = []
    for arg in args:
        product, price = arg
        if product not in grocery_list:
            continue
        if product not in bought:
            if price > budget:
                break
            budget -= price
            bought.append(product)

    if set(grocery_list) == set(bought):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        remaining_items = [item for item in grocery_list if item not in bought]
        return_string = f"You did not buy all the products. Missing products: {', '.join(remaining_items)}."
        return return_string


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))