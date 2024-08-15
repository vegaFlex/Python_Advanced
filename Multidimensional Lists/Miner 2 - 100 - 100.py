directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

def play_miner_game():
    field_size = int(input())
    commands = input().split()
    field = [input().split() for _ in range(field_size)]

    row_index, col_index = find_miner_position(field)
    collected_coal = count_coal(field)


    for command in commands:
        next_row, next_col = directions[command](row_index, col_index)

        if not is_valid_position(next_row, next_col, field_size):
            continue

        elif command == "up":
            row_index -= 1
        elif command == "down":
            row_index += 1
        elif command == "left":
            col_index -= 1
        elif command == "right":
            col_index += 1

        current_cell = field[row_index][col_index]

        if current_cell == "e":
            print(f"Game over! ({row_index}, {col_index})")
            return
        elif current_cell == "c":
            collected_coal -= 1
            field[row_index][col_index] = "*"

        if collected_coal == 0:
            print(f"You collected all coal! ({row_index}, {col_index})")
            return

    print(f"{collected_coal} pieces of coal left. ({row_index}, {col_index})")


def find_miner_position(field):
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell == "s":
                return i, j


def count_coal(field):
    count = 0
    for row in field:
        count += row.count("c")
    return count


def is_valid_position(row, col, field_size):
    return 0 <= row < field_size and 0 <= col < field_size


play_miner_game()