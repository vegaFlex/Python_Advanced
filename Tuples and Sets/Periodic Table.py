# n = int(input())
# elements = []
#
# for _ in range(n):
#     curr_elements = input().split()
#     elements.extend(curr_elements)
#
# print(*(set(elements)), sep='\n')

n = int(input())
elements = set()

for _ in range(n):
    current_set = set(input().split())
    elements = elements.union(current_set)

print(*elements, sep='\n')
