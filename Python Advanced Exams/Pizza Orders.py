pica_orders = [int(x) for x in input().split(', ')]
employs_capacity = [int(x) for x in input().split(', ')]

total_pizzas_made = 0
while pica_orders and employs_capacity:
    curr_order = pica_orders.pop(0)
    curr_employ_cpcty = employs_capacity.pop()

    if curr_order <= 0:
        employs_capacity.append(curr_employ_cpcty)
        continue

    if curr_order > 10:
        employs_capacity.append(curr_employ_cpcty)
        continue

    if curr_order <= curr_employ_cpcty:
        total_pizzas_made += curr_order

    elif curr_order > curr_employ_cpcty:
        total_pizzas_made += curr_employ_cpcty
        pica_orders.insert(0, (curr_order - curr_employ_cpcty))

if not pica_orders:
    print('All orders are successfully completed!')
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f'Employees: {", ".join(str(x) for x in employs_capacity)}')
else:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join(str(x) for x in pica_orders)}")



