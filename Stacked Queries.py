stack = []
queries = int(input())

for _ in range(queries):
    command = input()
    if command.split()[0] == '1':
        num_to_push = int(command.split()[1])
        stack.append(num_to_push)
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))

    