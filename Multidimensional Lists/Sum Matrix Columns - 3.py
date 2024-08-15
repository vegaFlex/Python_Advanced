rows, columns = [int(x)for x in input().split(', ')]
matrix = [[int(j) for j in input().split()] for i in range(rows)]

for column_idx in range(columns):
    sum_column = 0
    for row_idx in range(rows):
        sum_column += matrix[row_idx][column_idx]
    print(sum_column)

