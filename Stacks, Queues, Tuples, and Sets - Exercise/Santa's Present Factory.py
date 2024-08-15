from collections import deque

crafted_toys = {}

materials_values = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

toys_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
while materials_values and magic_values:
    curr_material = materials_values.pop()
    curr_magic = magic_values.popleft()

    if curr_material == 0 and curr_magic == 0:
        continue
    if curr_material == 0:
        magic_values.appendleft(curr_magic)
        continue
    if curr_magic == 0:
        materials_values.append(curr_material)
        continue

    result = curr_material * curr_magic

    if result in toys_table:
        toy_name = toys_table[result]

        if toy_name not in crafted_toys:
            crafted_toys[toy_name] = 0
        crafted_toys[toy_name] += 1
    else:
        if result < 0:
            materials_values.append(curr_material + curr_magic)
        else:
            materials_values.append(curr_material + 15)

if ('Doll' in crafted_toys and 'Wooden Train' in crafted_toys) or (
        'Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials_values:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials_values)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")
