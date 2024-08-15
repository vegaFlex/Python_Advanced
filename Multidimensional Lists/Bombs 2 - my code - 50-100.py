# 50/100 - jugde

n = int(input())
mtrx = [[int(j) for j in input().split()] for i in range(n)]
bombs_cord = input().split()


for i in range(n):
    for bomb in bombs_cord:
        row, col = [int(x) for x in bomb.split(',')]

        cordinates_children = [[row-1, col-1], [row-1, col], [row-1, col+1],
                               [row, col-1], [row, col], [row, col+1],
                               [row+1, col-1], [row+1, col], [row+1, col+1]]

        bomb_power = mtrx[row][col]
        bomb_idx = row, col
        mtrx[row][col] = 0

        for cordinates in cordinates_children:
            row1, col1 = cordinates

            if 0 <= row1 < len(mtrx) and 0 <= col1 < len(mtrx) and mtrx[row1][col1] > 0 and mtrx[row1][col1] != bomb_power:
                mtrx[row1][col1] -= bomb_power

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


