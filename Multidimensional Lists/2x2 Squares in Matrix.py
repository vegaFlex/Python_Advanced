rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]

match = 0

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        if matrix[row_idx][col_idx] == matrix[row_idx][col_idx + 1] == \
                matrix[row_idx + 1][col_idx] == matrix[row_idx + 1][col_idx + 1]:
            match += 1

print(match)


