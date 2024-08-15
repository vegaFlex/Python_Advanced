import string

alphabet_dict = dict(enumerate(string.ascii_lowercase))

rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    submatrix = []
    for col in range(cols):
        letter1 = alphabet_dict[row]
        letter2 = alphabet_dict[col + row]
        letter3 = alphabet_dict[row]

        submatrix.append(letter1 + letter2 + letter3)
    matrix.append(submatrix)

for curr_row in matrix:
    print(*curr_row)
