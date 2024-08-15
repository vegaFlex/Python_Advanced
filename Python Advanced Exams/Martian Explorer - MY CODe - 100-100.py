from collections import deque


def is_outside(r, c, mtrx_len):
    if r in range(mtrx_len) and c in range(mtrx_len):
        return False
    return True


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

found_deposits = {'W': 0, 'M': 0, 'C': 0}

while commands:
    curr_command = commands.popleft()

    next_row, next_col = directions[curr_command](rover_row, rover_col)

    if is_outside(next_row, next_col, n):
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

    if mtrx[rover_row][rover_col] == 'W':
        found_deposits['W'] += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")

    elif mtrx[rover_row][rover_col] == 'M':
        found_deposits['M'] += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")

    elif mtrx[rover_row][rover_col] == 'C':
        found_deposits['C'] += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")

if all(value > 0 for value in found_deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

