def find_match(chess_board, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
        [row + 1, col - 2],
        [row + 1, col + 2]
    ]

    touches = 0
    for r, c in moves:
        if r in range(len(chess_board)) and c in range(len(chess_board)) and chess_board[r][c] == 'K':
            touches += 1
    return touches


removed_player = 0

size = int(input())
chess_board = [list(input()) for _ in range(size)]

while True:
    best_horse, horse_row, horse_col = 0, 0, 0

    for row in range(size):
        for col in range(size):
            if chess_board[row][col] == '0':
                continue

            match = find_match(chess_board, row, col)

            if match > best_horse:
                best_horse, horse_row, horse_col = match, row, col

    if best_horse == 0:
        break

    chess_board[horse_row][horse_col] = '0'
    removed_player += 1

print(removed_player)

