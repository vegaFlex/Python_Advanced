mtrx = [[x for x in input().split()] for _ in range(5)]

my_row, my_col = 0, 0
target_cords = []

for row in range(5):
    for col in range(5):
        if mtrx[row][col] == 'A':
            my_row, my_col = row, col

        elif mtrx[row][col] == 'x':
            target_cords.append([row, col])

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

initial_targets_count = len(target_cords)
curr_targets_count = len(target_cords)
shooted_target = []
count_commands = int(input())

for _ in range(count_commands):
    commands = input().split()

    if curr_targets_count == 0:
        break

    if commands[0] == 'move':
        direction = commands[1]
        steps = int(commands[2])

        next_row, next_col = directions[direction](my_row, my_col)

        if not (next_row in range(len(mtrx)) and next_col in range(len(mtrx))):
            break

        for _ in range(steps):

            mtrx[my_row][my_col] = '.'
            my_row, my_col = next_row, next_col

            if mtrx[next_row][next_col] == 'x':
                shooted_target.append([next_row, next_col])

    elif commands[0] == 'shoot':
        direction = commands[1]

        next_row, next_col = directions[direction](my_row, my_col)

        if not (next_row in range(len(mtrx)) and next_col in range(len(mtrx))):
            break

        while True:
            if mtrx[my_row][my_row] == 'x':
                curr_targets_count -= 1
                shooted_target.append([my_row, my_col])
                mtrx[my_row][my_col] = '.'
                my_row, my_col = next_row, next_col
                break

            else:
                next_row, next_col = directions[direction](next_row, next_col)
                my_row, my_col = next_row, next_col

if curr_targets_count == 0:
    print(f"Training completed! All {initial_targets_count} targets hit.")
else:
    print(f"Training not completed! {curr_targets_count} targets left.")

[print(target) for target in shooted_target]