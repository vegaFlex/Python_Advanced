size = int(input())
field_mtrx = [[x for x in input().split()] for _ in range(size)]

direction = None
best_positions = None
possible_directions = {}
max_eggs = float('-inf')

for row in range(size):
    for col in range(size):
        curr_el = field_mtrx[row][col]
        if curr_el == 'B':
            idx_bunny = row, col

            up = []
            for idx in range(row - 1, -1, -1):
                r, c = idx, col
                up.append([r, c])
            possible_directions['up'] = up

            down = []
            for idx in range(row + 1, size):
                r, c = idx, col
                down.append([r, c])
            possible_directions['down'] = down

            left = []
            for idx in range(col - 1, -1, -1):
                r, c = row, idx
                left.append([r, c])
            possible_directions["left"] = left

            right = []
            for idx in range(col + 1, size):
                r, c = row, idx
                right.append([r, c])
            possible_directions["right"] = right

for key, values in possible_directions.items():
    sum_eggs = 0
    positions = []

    for el in values:
        curr_row, curr_col = el
        curr_pos = field_mtrx[curr_row][curr_col]

        if curr_pos == 'X':
            break

        egg = int(field_mtrx[curr_row][curr_col])
        sum_eggs += egg
        positions.append([curr_row, curr_col])

    if sum_eggs > max_eggs:
        max_eggs = sum_eggs
        best_positions = positions
        direction = key

print(direction)
[print(el) for el in best_positions]
print(max_eggs)
