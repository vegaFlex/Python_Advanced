rows, cols = [int(x) for x in input().split()]

matrix = [[j for j in input().split()] for i in range(rows)]

while True:
    line = input()
    if line == 'END':
        break

    line_parts = line.split()

    if line_parts[0] != 'swap' or len(line_parts) != 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]

    if row1 < 0 or row2 < 0 or col1 > cols or col2 > cols:
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    [print(*row) for row in matrix]
