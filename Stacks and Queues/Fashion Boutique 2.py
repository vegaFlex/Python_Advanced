sequence = [int(el) for el in input().split()]
rack_capacity = int(input())
rack_counter = 1
curr_capacity_rack = rack_capacity

while sequence:
    curr_clothes = sequence[-1]
    if curr_clothes <= curr_capacity_rack:
        curr_capacity_rack -= curr_clothes
        sequence.pop()
    else:
        rack_counter += 1
        curr_capacity_rack = rack_capacity

print(rack_counter)
