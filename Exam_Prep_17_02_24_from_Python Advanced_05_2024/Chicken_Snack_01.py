def henry_street_food(money_sequence, price_sequence):
    foods_eaten = 0

    while money_sequence and price_sequence:
        current_money = money_sequence.pop()
        current_price = price_sequence.pop(0)

        if current_money == current_price:
            foods_eaten += 1
        elif current_money > current_price:
            foods_eaten += 1
            change = current_money - current_price
            if money_sequence:
                money_sequence[-1] += change
        # If current_money < current_price, both are just removed without incrementing the counter

    if foods_eaten >= 4:
        print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
    elif foods_eaten > 1:
        print(f"Henry ate: {foods_eaten} foods.")
    elif foods_eaten == 1:
        print(f"Henry ate: {foods_eaten} food.")
    else:
        print("Henry remained hungry. He will try next weekend again.")


input_money_sequence = list(map(int, input().split()))
input_price_sequence = list(map(int, input().split()))

henry_street_food(input_money_sequence, input_price_sequence)
