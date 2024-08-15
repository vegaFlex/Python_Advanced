size_matrix = int(input())
matrix = [[int(j) for j in input().split()] for i in range(size_matrix)]

sum_diagonal = sum(matrix[size_matrix - i - 1][size_matrix - i - 1] for i in range(size_matrix))
print(sum_diagonal)

