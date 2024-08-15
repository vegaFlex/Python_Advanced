n = int(input())
matrix = [list(input()) for i in range(n)]
searched_symbol = input()
first_match = ()

for row_idx in range(n):
    for col_idx in range(n):
        a = matrix[row_idx][col_idx]

        if matrix[row_idx][col_idx] == searched_symbol:
            first_match += (row_idx, col_idx)

    if first_match:
        break

if first_match:
    print(first_match)

else:
    print(f"{searched_symbol} does not occur in the matrix")
