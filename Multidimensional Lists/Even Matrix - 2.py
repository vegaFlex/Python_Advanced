rows = int(input())
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
even = [[num for num in row if int(num) % 2 == 0] for row in matrix]

print(even)

