def get_children(matrix, row, col):
    posible_children = [
        [row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
        [row, col - 1], [row, col + 1],
        [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]
    ]

    result = []
    for child_row, child_col in posible_children:
        if child_row in range(len(matrix)) and child_col in range(len(matrix)) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


n = int(input())
mtrx = [[int(j) for j in input().split()] for i in range(n)]
bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]
    bomb_power = mtrx[row][col]

    if bomb_power <= 0:
        continue

    mtrx[row][col] = 0

    children = get_children(mtrx, row, col)

    for child_row, child_col in children:
        mtrx[child_row][child_col] -= bomb_power

alive_cells_count = 0
alive_cells_sum = 0

for row in mtrx:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells_count}')
print(f'Sum: {alive_cells_sum}')
[print(*row, sep=' ') for row in mtrx]




