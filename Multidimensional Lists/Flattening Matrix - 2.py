rows = int(input())
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
print([num for sublist in matrix for num in sublist])


# for _ in range(rows):
#     matrix.extend(int(x) for x in input().split(', '))
#
# print(matrix)

