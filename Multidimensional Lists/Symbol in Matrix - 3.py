n = int(input())
matrix = [list(input()) for i in range(n)]
searched_symbol = input()
first_match = None

for row in matrix:
    if searched_symbol in row:
        first_match = (matrix.index(row), row.index(searched_symbol))
        print(first_match)
        break

if not first_match:
    print(f"{searched_symbol} does not occur in the matrix")
