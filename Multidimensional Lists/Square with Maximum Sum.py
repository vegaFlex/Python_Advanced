import sys

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]

max_sum = -sys.maxsize
max_sum_matrix = []

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        sub_matrix = [matrix[row_idx][col_idx], matrix[row_idx][col_idx+1],
                      matrix[row_idx+1][col_idx], matrix[row_idx+1][col_idx+1]]

        curr_sum = sum(sub_matrix)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_matrix = sub_matrix.copy()

print(max_sum_matrix[0], max_sum_matrix[1])
print(max_sum_matrix[2], max_sum_matrix[3])
print(max_sum)


