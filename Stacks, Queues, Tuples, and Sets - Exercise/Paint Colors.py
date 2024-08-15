from collections import deque

sequence = deque(input().split())
main_colors = {"red", "yellow", "blue"}
second_colors = {"orange", "purple", "green"}

collected_colors = []

while sequence:
    first_el = sequence.popleft()
    last_el = sequence.pop() if sequence else ''

    union_el = first_el + last_el
    if union_el in main_colors or union_el in second_colors:
        collected_colors.append(union_el)
        continue

    union_el = last_el + first_el
    if union_el in main_colors or union_el in second_colors:
        collected_colors.append(union_el)
        continue

    first_el = first_el[:-1]
    last_el = last_el[:-1]

    if first_el:
        sequence.insert(len(sequence) // 2, first_el)
    if last_el:
        sequence.insert(len(sequence) // 2, last_el)

result = []

colors_ingredients = {
    "orange": ['red', 'yellow'],
    "purple": ['red', 'blue'],
    "green": ['yellow', 'blue']
}

for color in collected_colors:
    if color in main_colors:
        result.append(color)
        continue

    is_collected = True
    for curr_color in colors_ingredients[color]:
        if curr_color not in collected_colors:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)



