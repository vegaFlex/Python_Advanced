size_mtx = int(input())
matrix = [[int(j) for j in input().split()] for i in range(size_mtx)]

primary = []
secondary = []

for idx in range(size_mtx):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size_mtx-1 - idx])

difference = abs(sum(primary) - sum(secondary))
print(difference)
