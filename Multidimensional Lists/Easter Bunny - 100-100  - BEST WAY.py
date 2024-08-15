n = int(input())
mtrx = [[x for x in input().split()] for _ in range(n)]
bunny_row, bunny_col = 0, 0

for row in range(n):
    for col in range(n):
        if mtrx[row][col] == "B":
            bunny_row, bunny_col = row, col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

best_sum, best_dir, best_path = float('-inf'), '', []

for direction in directions:
    curr_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)
    curr_path = []

    while row in range(n) and col in range(n) and mtrx[row][col] != 'X':
        curr_sum += int(mtrx[row][col])
        curr_path.append([row, col])
        row, col = directions[direction](row, col)

    if curr_sum > best_sum and curr_path:
        best_sum, best_dir, best_path = curr_sum, direction, curr_path


print(best_dir)
print(*best_path, sep='\n')
print(best_sum)




