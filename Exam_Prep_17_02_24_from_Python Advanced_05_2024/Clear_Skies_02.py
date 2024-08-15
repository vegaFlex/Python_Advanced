def print_airspace(matrix):
    for row in matrix:
        print("".join(row))


def find_position(matrix, element):
    for i, row in enumerate(matrix):
        if element in row:
            return i, row.index(element)
    return None, None


def move_jetfighter(matrix, position, direction, armor, enemies_count):
    n = len(matrix)
    row, col = position
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    d_row, d_col = directions[direction]
    new_row, new_col = row + d_row, col + d_col

    if 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == '-':
            matrix[row][col] = '-'
            matrix[new_row][new_col] = 'J'
        elif matrix[new_row][new_col] == 'E':
            enemies_count -= 1
            armor -= 100
            matrix[row][col] = '-'
            matrix[new_row][new_col] = 'J'
            if enemies_count == 0:
                return armor, enemies_count, (
                    new_row, new_col), "Mission accomplished, you neutralized the aerial threat!"
            elif armor <= 0:
                return armor, enemies_count, (new_row,
                                              new_col), f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!"
        elif matrix[new_row][new_col] == 'R':
            armor = 300
            matrix[row][col] = '-'
            matrix[new_row][new_col] = 'J'

        return armor, enemies_count, (new_row, new_col), None

    return armor, enemies_count, position, None


def main():
    n = int(input().strip())
    matrix = [list(input().strip()) for _ in range(n)]

    position = find_position(matrix, 'J')
    armor = 300

    # Count enemies
    enemies_count = sum(row.count('E') for row in matrix)

    while True:
        direction = input().strip()
        armor, enemies_count, position, result = move_jetfighter(matrix, position, direction, armor, enemies_count)
        if result:
            print(result)
            break

    print_airspace(matrix)


if __name__ == "__main__":
    main()
