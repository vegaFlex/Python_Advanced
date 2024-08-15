rows, cols = [int(x) for x in input().split()]
matrix = [[j for j in input().split()]for i in range(rows)]

command = input()

while not command == 'END':
    commands = command.split()

    if commands[0] != 'swap' or len(commands[1:]) > 4:
        print('Invalid input!')

    else:
        row1, col1, row2, col2 = [int(x) for x in commands[1:]]

        if not (row1 in range(rows) and row2 in range(rows) or col1 in range(cols) and col2 in range(cols)):
            print('Invalid input!')
            command = input()
            continue

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for row in matrix:
            print(*row)

    command = input()

