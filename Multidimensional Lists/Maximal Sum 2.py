rows, columns = [int(num) for num in input().split()]
matrix = [[int(num) for num in input().split()] for i in range(rows)]

max_sum = float('-inf')
max_sum_submatrix = []

for i in range(rows - 2):
    for j in range(columns - 2):
        submatrix = [matrix[i + k][j:j + 3] for k in range(3)]
        submatrix_sum = sum(sum(row) for row in submatrix)

        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_sum_submatrix = submatrix

print(f"Sum = {max_sum}")
[print(*roww) for roww in max_sum_submatrix]

# for row in max_sum_submatrix:
#     print(' '.join(str(num) for num in row))


