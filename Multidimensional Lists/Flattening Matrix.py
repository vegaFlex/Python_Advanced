rows = int(input())
matrix = []

for _ in range(rows):
    matrix.extend([int(num) for num in input().split(', ')])

print(matrix)


# rows_count = int(input())
# matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
# flattened = [num for row in matrix for num in row]
# print(flattened)

