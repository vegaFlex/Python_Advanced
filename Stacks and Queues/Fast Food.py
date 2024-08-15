from collections import deque

food_qty = int(input())
queue = deque(int(el) for el in input().split())
biggest_order = max(queue)

while queue:
    num = queue[0]
    if num <= food_qty:
        food_qty -= num
        queue.popleft()
    else:
        break

print(biggest_order)
if not queue:
    print('Orders complete')
else:
    queue_str = ' '.join([str(el) for el in queue])
    print(f'Orders left: {queue_str}')
