n = int(input())
all_cars = set()

for _ in range(n):
    direction, car_numb = input().split(', ')

    if direction == 'IN':
        all_cars.add(car_numb)

    elif direction == 'OUT':
        all_cars.remove(car_numb)

if all_cars:
    print('\n'.join(all_cars))
else:
    print("Parking Lot is Empty")


