def math_operations(*args, **kwargs):
    result = kwargs.copy()

    for i, num in enumerate(args):
        if i == 0:
            result['a'] += num
        elif i == 1:
            result['s'] -= num
        elif i == 2:
            if num != 0:
                result['d'] /= num
        elif i == 3:
            result['m'] *= num

    sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join([f'{key}: {value:.1f}' for key, value in sorted_result])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))