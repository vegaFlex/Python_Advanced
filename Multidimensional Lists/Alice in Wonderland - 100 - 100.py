def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


n = int(input())
mtrx = [[j for j in input().split()] for i in range(n)]

alice_row, alice_col = 0, 0
for row in range(n):
    for col in range(n):
        if mtrx[row][col] == 'A':
            alice_row, alice_col = row, col

tea_bags = 0
while tea_bags < 10:
    mtrx[alice_row][alice_col] = '*'
    direction = input()
    next_row, next_col = get_next_pos(alice_row, alice_col, direction)

    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
        break
    alice_row, alice_col = next_row, next_col

    if mtrx[alice_row][alice_col] == '.' or mtrx[alice_row][alice_col] == '*':
        continue

    if mtrx[alice_row][alice_col] == 'R':
        break

    tea_bags += int(mtrx[alice_row][alice_col])

mtrx[alice_row][alice_col] = '*'

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in mtrx]


