line = input().split('|')
flat = []

for el in line[::-1]:
    for el2 in el.split():
        flat.append(el2)

print(*flat)

