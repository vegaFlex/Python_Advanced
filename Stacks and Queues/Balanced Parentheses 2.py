expression = input()
my_stack = []
balanced = True

for symbol in expression:
    if symbol in '[{(':
        my_stack.append(symbol)

    elif symbol in ')}]':
        if not my_stack:
            balanced = False
            break

        opening_bracket = my_stack.pop()

        if symbol == ')' and opening_bracket == '(':
            continue
        elif symbol == '}' and opening_bracket == '{':
            continue
        elif symbol == ']' and opening_bracket == '[':
            continue
        else:
            balanced = False
            break

if balanced and not my_stack:
    print('YES')
else:
    print('NO')

