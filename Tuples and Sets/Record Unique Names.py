names_count = int(input())
names = set()

for _ in range(names_count):
    curr_name = input()
    names.add(curr_name)
print('\n'.join(names))

# print(*names, sep='\n')- correct
