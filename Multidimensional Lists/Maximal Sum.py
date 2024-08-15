rows, cols = [int(x) for x in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(rows)]

max_sum = float('-inf')
max_submatrix = None

for row in range(rows - 2):
    for col in range(cols - 2):
        submatrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                     matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                     matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]

        sum_submatrix = sum(submatrix)
        if sum_submatrix > max_sum:
            max_sum = sum_submatrix
            max_submatrix = submatrix.copy()

print(f"Sum = {max_sum}")
print(max_submatrix[0], max_submatrix[1], max_submatrix[2])
print(max_submatrix[3], max_submatrix[4], max_submatrix[5])
print(max_submatrix[6], max_submatrix[7], max_submatrix[8])

