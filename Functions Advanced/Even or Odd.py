def even_odd(*args):
    command = args[-1]

    return [num for num in args[:-1] if num % 2 == 0] if command == 'even' \
        else [num for num in args[:-1] if num % 2 == 1]



# solution 2
# def even_odd(*args):
#     command = args[-1]
#     parity = 0 if command == 'even' else 1
#     result = []
#     for num in (args[:-1]):
#         if num % 2 == parity:
#             result.append(num)
#
#     return result

# solution 3
# my_code:
#
# def even_odd(*numbers):
#     command = numbers[-1]
#
#     if command == "even":
#         return [num for num in numbers[:-1] if num % 2 == 0]
#     elif command == "odd":
#         return [num for num in numbers[:-1] if num % 2 == 1]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
# print(even_odd(1, 2, 3, 4, 5, 6, 'odd'))