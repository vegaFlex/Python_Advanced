def operate(operator, *args):
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
    elif operator == "/":
        result = args[0]
        for arg in args[1:]:
            result /= arg
    else:
        raise ValueError("Invalid operator")
    return result


# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("-", 3, 4, 5, 2, 1))
# print(operate("/", 3, 4, 5, 2))

