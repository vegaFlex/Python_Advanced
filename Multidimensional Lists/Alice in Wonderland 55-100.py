n = int(input())
mtrx = [[j for j in input().split()] for i in range(n)]

alisa_row, alisa_col = 0, 0

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

for row in range(n):
    for col in range(n):
        if mtrx[row][col] == 'A':
            alisa_row, alisa_col = row, col

tea = 0
while tea < 10:
    command = input()
    next_row, next_col = directions[command](alisa_row, alisa_col)
    next_el = mtrx[next_row][next_col]
    mtrx[alisa_row][alisa_col] = '*'

    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
        break

    if next_el.isdigit():
        tea += int(mtrx[next_row][next_col])

    elif next_el == 'R':
        mtrx[next_row][next_col] = '*'
        print("Alice didn't make it to the tea party.")
        [print(*row) for row in mtrx]
        break

    alisa_row, alisa_col = next_row, next_col

if tea > 9:
    mtrx[alisa_row][alisa_col] = '*'
    print("She did it! She went to the party.")
    [print(*row) for row in mtrx]
