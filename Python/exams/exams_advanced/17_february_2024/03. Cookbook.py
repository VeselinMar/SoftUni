def cookbook(*args):
    cookbook_dictionary = {}
    for arg in args:
        recipe_name, cuisine, ingredients_list = arg
        if cuisine not in cookbook_dictionary:
            cookbook_dictionary[cuisine] = {recipe_name: ingredients_list}
        else:
            cookbook_dictionary[cuisine][recipe_name] = ingredients_list

    return_text = []
    for item in sorted(cookbook_dictionary.items(), key=lambda x: (-len(x[1]), x[0])):
        return_text.append(f"{item[0]} cuisine contains {len(item[1])} recipes:")
        for recipe_name, ingredients_list in sorted(item[1].items()):
            return_text.append(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients_list)}")

    return '\n'.join(return_text)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
