first = set([int(num) for num in input().split()])
second = set([int(num) for num in input().split()])
n = int(input())

for _ in range(n):
    commands = input().split()
    curr_command = commands[0]
    sequence = commands[1]

    if curr_command == 'Add':
        if sequence == 'First':
            first = first.union([int(num) for num in commands[2:]])
        elif sequence == 'Second':
            second = second.union([int(num) for num in commands[2:]])

    elif curr_command == 'Remove':
        if sequence == 'First':
            first = first.difference([int(num) for num in commands[2:]])
        elif sequence == 'Second':
            second = second.difference([int(num) for num in commands[2:]])

    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')

