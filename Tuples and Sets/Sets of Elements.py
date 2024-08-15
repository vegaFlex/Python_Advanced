# n, m = [int(num) for num in input().split()]
# first_set = set(int(input())for num in range(n))
# second_set = set(int(input())for num in range(m))
# intersection_elements = first_set.intersection(second_set)
# print(*intersection_elements, sep='\n')

n, m = [int(num) for num in input().split()]
first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(int(input()))

for _ in range(m):
    second_set.add(int(input()))

intersection_elements = first_set.intersection(second_set)
print(*intersection_elements, sep='\n')
