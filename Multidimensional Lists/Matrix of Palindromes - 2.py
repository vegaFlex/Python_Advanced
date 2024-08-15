import string

r, c = [int(x)for x in input().split()]
mtrx = []

alpha_dict = dict(enumerate(string.ascii_lowercase))

for i in range(r):
    cur_row = []
    for j in range(c):
        word = alpha_dict[i]+alpha_dict[j+i]+alpha_dict[i]
        cur_row.append(word)

    mtrx.append(cur_row)
    print(*cur_row)
