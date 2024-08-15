rows, columns = [int(x)for x in input().split(', ')]
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
sum_matrix = sum([sum(el) for el in matrix])

print(sum_matrix)
print(matrix)