# import math

def is_outside(r, c, matrix):
    if r in range(len(matrix)) and c in range(len(matrix)):
        return False
    return True


n = int(input())
mtrx = [[x for x in input().split()] for _ in range(n)]

player_row, player_col = 0, 0
for row in range(n):
    for col in range(n):
        if mtrx[row][col] == 'P':
            player_row, player_col = row, col

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

coins = 0
path = []
path.append([player_row, player_col])
mtrx[player_row][player_col] = '0'

won = True

while True:
    if coins >= 100:
        break

    command = input()

    next_row, next_col = directions[command](player_row, player_col)

    if not is_outside(next_row, next_col, mtrx):

        if mtrx[next_row][next_col] == 'X':
            path.append([next_row, next_col])
            won = False
            coins //= 2
            # coins = math.floor(coins)
            break

    if next_row < 0:
        next_row = n - 1
    if next_col < 0:
        next_col = n - 1
    if next_row >= n:
        next_row = 0
    if next_col >= n:
        next_col = 0

    # player_row, player_col = next_row, (next_col % n)
    player_row, player_col = next_row, next_col
    path.append([player_row, player_col])
    coins += int(mtrx[player_row][player_col])
    mtrx[player_row][player_col] = '0'

if won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print('Your path:')
print('\n'.join([str(x) for x in path]))


