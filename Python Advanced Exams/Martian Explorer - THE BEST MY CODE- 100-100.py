from collections import deque

n = 6
mtrx = [[x for x in input().split()] for _ in range(n)]

commands = deque(input().split(', '))

rover_row, rover_col = 0, 0
for row_i in range(n):
    for col_i in range(n):
        if mtrx[row_i][col_i] == 'E':
            rover_row, rover_col = row_i, col_i

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

found_deposits = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}

while commands:
    curr_command = commands.popleft()

    next_row, next_col = directions[curr_command](rover_row, rover_col)

    if next_row < 0:
        next_row = n - 1
    if next_col < 0:
        next_col = n - 1
    if next_row >= n:
        next_row = 0
    if next_col >= n:
        next_col = 0

    if mtrx[next_row][next_col] == 'R':
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    rover_row, rover_col = next_row, next_col

    if mtrx[rover_row][rover_col] in ['W', 'M', 'C']:

        curr_elmnt = mtrx[rover_row][rover_col]
        found_deposits[curr_elmnt][1] += 1
        print(f"{found_deposits[curr_elmnt][0]} deposit found at ({rover_row}, {rover_col})")


if all(value[1] > 0 for value in found_deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
