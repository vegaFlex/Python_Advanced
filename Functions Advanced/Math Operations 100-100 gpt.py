def math_operations(*args, **kwargs):
    result_dict = kwargs.copy()
    operations = {
        'a': lambda x, y: x + y,
        's': lambda x, y: x - y,
        'd': lambda x, y: None if y == 0 else x / y,
        'm': lambda x, y: x * y,
    }
    for i, arg in enumerate(args):
        key = list(result_dict.keys())[i % len(result_dict)]
        operation = operations.get(key)

        if operation:
            new_value = operation(result_dict[key], arg)

            if new_value is not None:
                result_dict[key] = new_value

    sorted_items = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f'{key}: {value:.1f}' for key, value in sorted_items)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

