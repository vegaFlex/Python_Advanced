mtrx = [[x for x in input().split()] for _ in range(5)]

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
my_row, my_col = 0, 0
targets_cord = []

for row in range(5):
    for col in range(5):
        if mtrx[row][col] == 'A':
            my_row, my_col = row, col
        elif mtrx[row][col] == 'x':
            targets_cord.append([row, col])

mtrx[my_row][my_col] = '.'

initial_targets_len = len(targets_cord)
curr_targets_len = initial_targets_len

shooting_targets_cord = []

commands_count = int(input())
for _ in range(commands_count):
    commands = input().split()
    direction = commands[1]

    if curr_targets_len == 0:
        break

    next_row, next_col = directions[direction](my_row, my_col)

    if commands[0] == 'move':
        steps = int(commands[2])

        for _ in range(steps):
            next_row, next_col = directions[direction](my_row, my_col)
            if next_row not in range(len(mtrx)) or next_col not in range(len(mtrx)):
                break

            if mtrx[next_row][next_col] == '.':
                my_row, my_col = directions[direction](my_row, my_col)
                next_row, next_col = directions[direction](my_row, my_col)
            else:
                break

    elif commands[0] == 'shoot':
        while True:
            if next_row not in range(len(mtrx)) or next_col not in range(len(mtrx)):
                break

            if mtrx[next_row][next_col] == 'x':
                mtrx[next_row][next_col] = '.'
                # my_row, my_col = directions[direction](my_row, my_col)
                curr_targets_len -= 1
                shooting_targets_cord.append([next_row, next_col])
                break
            else:
                # my_row, my_col = directions[direction](my_row, my_col)
                next_row, next_col = directions[direction](next_row, next_col)

if curr_targets_len == 0:
    print(f"Training completed! All {initial_targets_len} targets hit.")
else:
    print(f"Training not completed! {curr_targets_len} targets left.")

[print(target) for target in shooting_targets_cord]

