# def operate(operator, *nums):
#     if operator == '+':
#         result = sum(nums)
#     elif operator == '-':
#         result = nums[0] - sum(nums[1:])
#     elif operator == '*':
#         result = 1
#         for num in nums:
#             result *= num
#     elif operator == '/':
#         result = nums[0]
#         for num in nums[1:]:
#             result /= num
#
#     return result

from functools import reduce


def operate(operator, *nums):
    if operator == '+':
        return reduce(lambda x, y: x + y, nums)
    elif operator == '-':
        return reduce(lambda x, y: x - y, nums)
    elif operator == '*':
        return reduce(lambda x, y: x * y, nums)
    else:
        return reduce(lambda x, y: x / y, nums)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 1, 2, 3))
print(operate("/", 1, 2, 3))
