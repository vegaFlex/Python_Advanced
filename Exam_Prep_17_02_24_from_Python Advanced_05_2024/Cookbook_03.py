def cookbook(*recipes):
    from collections import defaultdict

    cuisines = defaultdict(list)
    for recipe in recipes:
        name, cuisine, ingredients = recipe
        cuisines[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0]))

    output = []
    for cuisine, recipes_list in sorted_cuisines:
        output.append(f"{cuisine} cuisine contains {len(recipes_list)} recipes:")

        for recipe_name, ingredients in sorted(recipes_list):
            ingredients_str = ", ".join(ingredients)
            output.append(f"  * {recipe_name} -> Ingredients: {ingredients_str}")

    return "\n".join(output)


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))
