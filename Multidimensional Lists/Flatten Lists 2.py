# line = input()
# for part in line.split("|")[::-1]:
#     for el in part.split():
#         print(el, end=' ')

# line = input().split('|')
# flat = []
#
# for el in line[::-1]:
#     for el2 in el.split():
#         flat.append(el2)
#
# print(*flat)

# line = input()
# flatten = []
# for el in line.split('|')[::-1]:
#     flatten.extend(el.split())
#
# print(*flatten)

# mtrx = [elmnts.split() for elmnts in input().split("|")[::-1]]
# print(*sum(mtrx, [])) - correct
# print(*[element for row in mtrx for element in row])

# mtrx = [elmnts.split() for elmnts in input().split('|')[::-1]]
# print(mtrx)
# print(*[element for row in mtrx for element in row])
