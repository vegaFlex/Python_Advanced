from collections import deque

chocolates = deque([int(num) for num in input().split(', ')])
cups_of_milk = deque([int(num) for num in input().split(', ')])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:

    curr_chocolate = chocolates.pop()
    curr_milk = cups_of_milk.popleft()

    if curr_chocolate <= 0 and curr_milk <= 0:
        continue
    if curr_chocolate <= 0:
        cups_of_milk.appendleft(curr_milk)
        continue
    if curr_milk <= 0:
        chocolates.append(curr_chocolate)
        continue

    if curr_chocolate == curr_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(curr_milk)
        chocolates.append(curr_chocolate-5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")




