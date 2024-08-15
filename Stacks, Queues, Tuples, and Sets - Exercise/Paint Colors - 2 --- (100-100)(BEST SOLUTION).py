from collections import deque

string = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

collected_colors = []

while string:
    first_el = string.popleft()
    last_el = string.pop() if string else ''

    result = first_el + last_el
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = last_el + first_el
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    first_el = first_el[:-1]
    last_el = last_el[:-1]

    if first_el:
        string.insert(len(string) // 2, first_el)
    if last_el:
        string.insert(len(string) // 2, last_el)

final_colors = []

ingredients_secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for curr_color in collected_colors:
    if curr_color in main_colors or set(
            ingredients_secondary_colors[curr_color]).issubset(set(collected_colors)):
        final_colors.append(curr_color)

print(final_colors)
