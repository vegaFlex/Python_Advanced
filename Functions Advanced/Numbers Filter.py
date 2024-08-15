# SOLUTION 1:
def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if key == 'odd':
            result['odd'] = [num for num in value if num % 2 != 0]

        elif key == 'even':
            result['even'] = [num for num in value if num % 2 == 0]

    result = dict(sorted(result.items(), key=lambda x: -len(x[1])))

    return result

# SOLUTION2: CORRECT:
# def even_odd_filter(**kwargs):
#     even_nums = []
#     odd_nums = []
#
#     for key, value in kwargs.items():
#         if key == 'even':
#             even_nums = [num for num in value if num % 2 == 0]
#         elif key == 'odd':
#             odd_nums = [num for num in value if num % 2 != 0]
#
#     sorted_dict = sorted(kwargs.items(), key=lambda x: -len(x[1]))
#
#     result = {}
#     for key, value in sorted_dict:
#         if key == 'even':
#             result[key] = even_nums
#         elif key == 'odd':
#             result[key] = odd_nums
#
#     return result


# INPUT:
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))


# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))


# SOLUTION 3:
# def even_odd_filter(**kwargs):
#     even = []
#     odd = []
#
#     for key, values in kwargs.items():
#         for num in values:
#             if num % 2 == 0:
#                 even.append(num)
#
#             else:
#                 odd.append(num)
#
#     return f"'even': {even}, 'odd': {odd}"
