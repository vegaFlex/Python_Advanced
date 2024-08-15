def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    basket = []
    total_spent = 0

    for product, (price, quantity) in products.items():
        if len(basket) >= 5 or total_spent >= budget:
            break

        cost = price * quantity
        if total_spent + cost <= budget:
            basket.append(product)
            total_spent += cost
            print(f"You bought {product} for {cost:.2f} leva.")

    return ""


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print("______________________")
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print("______________________")
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
