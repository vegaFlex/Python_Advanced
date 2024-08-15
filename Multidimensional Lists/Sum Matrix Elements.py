rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    sum_matrix += sum(lines)
    matrix.append(lines)

print(sum_matrix)
print(matrix)

