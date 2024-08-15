def moves(cmnd, r, c):
    if cmnd == "up":
        return r - 1, c
    if cmnd == "down":
        return r + 1, c
    if cmnd == "left":
        return r, c - 1
    return r, c + 1


def is_inside(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


presents = int(input())
size = int(input())

matrix = []

santa_row, santa_col = 0, 0
nice_kids_count = 0
for row in range(size):
    elements = input()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'S':
            santa_row, santa_col = row, col
        if element == "V":
            nice_kids_count += 1

nice_with_gifts = 0
while True:
    command = input()
    if command == 'Christmas morning' or presents == 0:
        break
    next_row, next_col = moves(command, santa_row, santa_col)
    if is_inside(next_row, next_col, size):
        if matrix[next_row][next_col] == "V":
            nice_kids_count += 1
            presents -= 1

        elif matrix[next_row][next_col] == "X":
            santa_row, santa_col = next_row, next_col
        elif matrix[next_row][next_col] == "V":
            santa_row, santa_col = next_row, next_col
            presents -= 1
            nice_with_gifts += 1
        elif matrix[next_row][next_col] == "C":
            santa_row, santa_col = next_row, next_col
            matrix[santa_row][santa_col] = "S"
            if matrix[santa_row - 1][santa_col] == "V":
                presents -= 1
                nice_with_gifts += 1
                matrix[santa_row-1][santa_col] = '-'
            elif matrix[santa_row - 1][santa_col] == "X":
                presents -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == "V":
                presents -= 1
                nice_with_gifts += 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == "X":
                presents -= 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row][santa_col - 1] == "V":
                presents -= 1
                nice_with_gifts += 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col - 1] == "X":
                presents -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col + 1] == "V":
                presents -= 1
                nice_with_gifts += 1
                matrix[santa_row][santa_col + 1] = '-'
            elif matrix[santa_row][santa_col + 1] == "X":
                presents -= 1
                matrix[santa_row][santa_col + 1] = '-'
            if presents == 0:
                break


if nice_kids_count - nice_with_gifts > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))
