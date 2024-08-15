import os

try:
    with open('numbers.txt') as file:
        print(sum([int(line_num) for line_num in file.readlines()]))
        # _________________________
        # CORRECT:
        # result = 0
        # for line in file.readlines():
        #     result += int(line)
        # print(result)
        # ____________________________
except FileNotFoundError:
    print('File not found')

