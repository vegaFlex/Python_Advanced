def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'

    counter = 0
    buy_prod = []
    for product, values in kwargs.items():
        if counter == 5:
            break

        price, count = values
        total = price * count
        if total <= budget:
            budget -= total
            counter += 1
            buy_prod.append(f"You bought {product} for {total:.2f} leva.")

    return '\n'.join(buy_prod)


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
