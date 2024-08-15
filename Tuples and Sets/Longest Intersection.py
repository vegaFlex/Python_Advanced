n = int(input())
longest_intersection = set()

for _ in range(n):
    first_data, second_data = input().split('-')

    first_start, first_end = [int(num) for num in first_data.split(',')]
    second_start, second_end = [int(num) for num in second_data.split(',')]

    # first_set = set([el for el in range(first_start, first_end+1)]) -  correct
    # second_set = set([el for el in range(second_start, second_end+1)]) - correct

    first_set = set(range(first_start, first_end+1))
    second_set = set(range(second_start, second_end+1))

    curr_intersection = first_set.intersection(second_set)

    if len(curr_intersection) > len(longest_intersection):
        longest_intersection = curr_intersection

# print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")  - correct
print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")

