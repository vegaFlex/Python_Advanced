line = input().split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]


ingridients_second_color = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue'),
}

colected_colors = []
final_colors = []

while line:
    first = line.pop(0)
    last = line.pop() if line else ''

    if first+last in main_colors or first+last in secondary_colors:
        colected_colors.append(first + last)

    elif last+first in main_colors or last+first in secondary_colors:
        colected_colors.append(last+first)

    else:
        first = first[:-1]
        last = last[:-1]

        if first:
            line.insert(len(line)//2, first)
        if last:
            line.insert(len(line) // 2, last)


for color in colected_colors:
    if color in ingridients_second_color:
        if set(ingridients_second_color[color]).issubset(set(colected_colors)):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)