def is_outside(row, col, matrix):
    if row not in range(len(matrix)) or col not in range(len(matrix)):
        return True

    return False


n = int(input())
commands = input().split()
mtrx = [[x for x in input().split()] for i in range(n)]

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

collected_coals = 0
all_coal = 0

miner_row, miner_col = 0, 0
for row in range(n):
    for col in range(n):

        if mtrx[row][col] == 'c':
            all_coal += 1

        if mtrx[row][col] == 's':
            miner_row, miner_col = row, col

for cmnd in commands:
    next_row, next_col = directions[cmnd](miner_row, miner_col)

    if not is_outside(next_row, next_col, mtrx):

        if mtrx[next_row][next_col] == '*':
            miner_row, miner_col = next_row, next_col
            continue

        if mtrx[next_row][next_col] == 'e':
            print(f"Game over! ({next_row}, {next_col})")
            break

        if mtrx[next_row][next_col] == 'c':
            collected_coals += 1
            mtrx[next_row][next_col] = '*'
            miner_row, miner_col = next_row, next_col

            if all_coal == collected_coals:
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                break

else:
    print(f"{all_coal - collected_coals} pieces of coal left. ({miner_row}, {miner_col})")
