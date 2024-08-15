def get_next_position(dirctn, r, c, step):
    if dirctn == 'up':
        return r - step, c
    if dirctn == 'down':
        return r + step, c
    if dirctn == 'left':
        return r, c - step
    return r, c + step


def is_outside(r, c, s):
    if r < 0 or c < 0 or r >= s or c >= s:
        return True
    return False


size = 5
matrix = []
player_row, player_col = 0, 0
targets_count = 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            player_row, player_col = row, col
        if element == 'x':
            targets_count += 1

matrix[player_row][player_col] == '.'
hit_targets = []

number_of_commands = int(input())
for _ in range(number_of_commands):
    line_args = input().split()
    command = line_args[0]
    direction = line_args[1]

    if command == 'move':
        steps = int(line_args[2])
        next_row, next_col = get_next_position(direction, player_row, player_col, steps)

        if not is_outside(next_row, next_col, size) and matrix[next_row][next_col] == '.':
            player_row, player_col = next_row, next_col

    else:
        bullet_row, bullet_col = get_next_position(direction, player_row, player_col, 1)

        while not is_outside(bullet_row, bullet_col, size):
            if matrix[bullet_row][bullet_col] == 'x':
                targets_count -= 1
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break

            bullet_row, bullet_col = get_next_position(direction, bullet_row, bullet_col, 1)

        if targets_count == 0:
            break

if targets_count == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets_count} targets left.")

[print(target) for target in hit_targets]
