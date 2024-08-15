def play_miner_game():
    field_size = int(input())
    commands = input().split()
    field = []
    miner_position = None
    coal_count = 0

    for _ in range(field_size):
        row = input().split()
        field.append(row)
        if 's' in row:
            miner_position = (field.index(row), row.index('s'))
        coal_count += row.count('c')

    for command in commands:
        if command == 'up':
            next_position = (miner_position[0] - 1, miner_position[1])
        elif command == 'down':
            next_position = (miner_position[0] + 1, miner_position[1])
        elif command == 'left':
            next_position = (miner_position[0], miner_position[1] - 1)
        elif command == 'right':
            next_position = (miner_position[0], miner_position[1] + 1)

        if (
            next_position[0] < 0 or next_position[0] >= field_size or
            next_position[1] < 0 or next_position[1] >= field_size
        ):
            continue

        next_cell = field[next_position[0]][next_position[1]]

        if next_cell == 'e':
            print(f"Game over! ({next_position[0]}, {next_position[1]})")
            return
        elif next_cell == 'c':
            coal_count -= 1
            field[next_position[0]][next_position[1]] = '*'

        miner_position = next_position

        if coal_count == 0:
            print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
            return

    print(f"{coal_count} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")


play_miner_game()