size_matrix = int(input())
matrix = [[int(j) for j in input().split()] for i in range(size_matrix)]

sum_diagonal = 0

for i in range(size_matrix):
    curr_num = matrix[i][i]
    sum_diagonal += curr_num
print(sum_diagonal)
