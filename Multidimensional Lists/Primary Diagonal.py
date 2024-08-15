n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

diagonal = 0

for index in range(n):
    diagonal += matrix[index][index]

print(diagonal)

# size = int(input())
# matrix = [[0] * size for row in range(0, size)]
#
# for x in range(0, size):
#     line = list(map(int, input().split()))
#     for y in range(0, size):
#         matrix[x][y] = line[y]
#
# sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
# print(sum_diagonal)
