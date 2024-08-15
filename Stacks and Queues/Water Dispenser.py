from collections import deque

initial_water = int(input())
line = input()
queue = deque()

while not line == 'Start':
    queue.append(line)
    line = input()

command = input()
while not command == 'End':
    if command.isdigit():
        curr_liters = int(command)
        name = queue.popleft()
        if initial_water >= curr_liters:
            initial_water -= curr_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    elif 'refill' in command:
        liters_to_refill = int(command.split()[1])
        initial_water += liters_to_refill
    command = input()

print(f"{initial_water} liters left")