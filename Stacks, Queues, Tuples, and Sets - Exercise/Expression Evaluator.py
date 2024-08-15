from collections import deque

string = input().split()
nums = deque()

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for symbol in string:
    if symbol in '+-*/':
        while len(nums) > 1:
            first_num = int(nums.popleft())
            second_num = int(nums.popleft())
            result = operators[symbol](first_num, second_num)
            nums.appendleft(result)
    else:
        nums.append(int(symbol))

print(nums.popleft())

