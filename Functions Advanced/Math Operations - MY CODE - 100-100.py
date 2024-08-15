def math_operations(*args, **kwargs):
    result = kwargs.copy()

    for i, num in enumerate(args):

        key = list(result.keys())[i % len(result)]

        if key == 'a':
            result['a'] += num
        elif key == 's':
            result['s'] -= num
        elif key == 'd':
            if num != 0:
                result['d'] /= num
        elif key == 'm':
            result['m'] *= num

    # SOLUTION_2 - CORRECT
    # operations = {
    #     'a': lambda x, y: x + y,
    #     's': lambda x, y: x - y,
    #     'd': lambda x, y: None if y == 0 else x / y,
    #     'm': lambda x, y: x * y,
    # }
    #
    # key = list(result.keys())[i % len(result)]
    # operation = operations.get(key)
    # new_value = operation(result[key], num)
    # 
    # if new_value is not None:
    #     result[key] = new_value

    sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join([f'{key}: {value:.1f}' for key, value in sorted_result])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

