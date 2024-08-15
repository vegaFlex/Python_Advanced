clothes = [int(x) for x in input().split()]
capacity_rack = int(input())
rack_counter = 1
curr_capacity_rack = capacity_rack

while clothes:
    piece_of_clothing = clothes[-1]
    if piece_of_clothing > curr_capacity_rack:
        rack_counter += 1
        curr_capacity_rack = capacity_rack
    else:
        curr_capacity_rack -= piece_of_clothing
        clothes.pop()

print(rack_counter)


