rows = int(input())
matrix = []

for _ in range(rows):
    nums = [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    matrix.append(nums)

print(matrix)


# rows = int(input())
# matrix = []
#
# for i in range(rows):
#     row = input().split(", ")
#     matrix.append(list(map(int, row)))
# evens = [[x for x in row if x % 2 == 0] for row in matrix]

# print(evens)
