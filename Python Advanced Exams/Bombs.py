from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = deque([int(x) for x in input().split(', ')])

table_bombs = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}

is_collected_pouch = False
counter = 9

bombs_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

while bomb_effects and bomb_casings and not is_collected_pouch:
    curr_effect = bomb_effects.popleft()
    curr_casing = bomb_casings.pop()

    bomb_power = curr_effect + curr_casing

    if bomb_power in table_bombs:
        bombs_pouch[table_bombs[bomb_power]] += 1

        if bombs_pouch[table_bombs[bomb_power]] < 4:
            counter -= 1

        if counter == 0:
            is_collected_pouch = True

    else:
        bomb_effects.appendleft(curr_effect)
        bomb_casings.append(curr_casing - 5)

if is_collected_pouch:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

print('\n'.join([f"{k}: {v}" for k, v in sorted(bombs_pouch.items())]))

