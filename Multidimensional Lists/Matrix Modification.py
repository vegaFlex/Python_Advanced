size = int(input())
mtrx = [[int(j) for j in input().split()] for i in range(size)]

while True:
    line = input()

    if line == 'END':
        break

    commands = line.split()

    command = commands[0]
    row, col, value = [int(x) for x in commands[1:]]

    if not (row in range(size) and col in range(size)):
        print("Invalid coordinates")
        continue

    if command == 'Add':
        mtrx[row][col] += value
    elif command == 'Subtract':
        mtrx[row][col] -= value

[print(*row) for row in mtrx]


