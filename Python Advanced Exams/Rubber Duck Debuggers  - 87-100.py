from collections import deque


def rubber_ducky_table(res):
    if res in range(0, 60):
        return 'Darth Vader Ducky'
    elif res in range(61, 120):
        return 'Thor Ducky'
    elif res in range(121, 180):
        return 'Big Blue Rubber Ducky'
    elif res in range(181, 240):
        return 'Small Yellow Rubber Ducky'
    else:
        return None


time_to_complete_single_tasks = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

collected_ducky = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while time_to_complete_single_tasks and number_of_tasks:
    curr_time = time_to_complete_single_tasks.popleft()
    curr_task = number_of_tasks.pop()

    result = curr_time * curr_task

    curr_ducky = rubber_ducky_table(result)

    if curr_ducky is not None:
        collected_ducky[curr_ducky] += 1
    else:
        number_of_tasks.append(curr_task - 2)
        time_to_complete_single_tasks.append(curr_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f'{k}: {v}') for k, v in collected_ducky.items()]
