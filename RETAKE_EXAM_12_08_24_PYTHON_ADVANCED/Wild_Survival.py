def bee_battle(bees, bee_eaters):
    while bees and bee_eaters:
        current_bees = bees[0]
        current_bee_eaters = bee_eaters[-1]

        # Fight
        while current_bees > 0 and current_bee_eaters > 0:
            if current_bee_eaters * 7 >= current_bees:
                current_bee_eaters -= current_bees // 7
                current_bees = 0
            else:
                current_bees -= current_bee_eaters * 7
                current_bee_eaters = 0

        if current_bees == 0 and current_bee_eaters == 0:
            bees.pop(0)
            bee_eaters.pop()
        elif current_bees == 0:
            bees.pop(0)
            bee_eaters[-1] = current_bee_eaters
        elif current_bee_eaters == 0:
            bee_eaters.pop()
            bees.append(current_bees)
            bees.pop(0)

    print("The final battle is over!")
    if not bees and not bee_eaters:
        print("But no one made it out alive!")
    elif bees:
        print(f"Bee groups left: {', '.join(map(str, bees))}")
    elif bee_eaters:
        print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")


# Example input
bees = list(map(int, input().split()))
bee_eaters = list(map(int, input().split()))

bee_battle(bees, bee_eaters)
