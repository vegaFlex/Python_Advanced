rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for cow in range(columns):
    sum_col = 0
    for row in range(rows):
        sum_col += (matrix[row][cow])
    print(sum_col)

