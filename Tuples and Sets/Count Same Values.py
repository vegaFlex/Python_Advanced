numbers = [float(x) for x in input().split()]
occur = {}

for num in numbers:
    if num not in occur:
        occur[num] = 0
    occur[num] += 1

for key, value in occur.items():
    print(f"{key:.1f} - {value} times")

