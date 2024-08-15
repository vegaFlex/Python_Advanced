from collections import deque
from datetime import timedelta


class Robot:
    def __init__(self, name, process_time):
        self.name = name
        self.process_time = process_time
        self.busy = False
        self.pickup_time = int()


robot_input = input().split(';')
robots_q = deque()
products = deque()
starting_time = input()


def get_sec(starting_time):
    h, m, s = starting_time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def get_time(secs):
    time = timedelta(seconds=secs)
    return time


for robo in robot_input:
    robot = robo.split('-')
    robots_q.append(Robot(robot[0], int(robot[1])))

while True:
    product = input()
    if product == 'End':
        break

    products.append(product)

current_time = get_sec(starting_time)
while True:
    active_product = True
    if not products:
        break

    current_robot = robots_q[0]
    current_product = products.popleft()

    if not current_robot.busy:
        robots_q.popleft()
        current_robot.busy = True
        current_time += 1
        current_robot.pickup_time = current_time

        robots_q.append(current_robot)
        print(f"{current_robot.name} - {current_product} [0{get_time(current_time)}]")
    else:
        current_time += 1

        for robot in robots_q:
            if current_time - robot.pickup_time == robot.process_time:
                print(f"{robot.name} - {current_product} [0{get_time(current_time)}]")
                robot.pickup_time = current_time
                active_product = False
        if active_product:
            products.append(current_product)

