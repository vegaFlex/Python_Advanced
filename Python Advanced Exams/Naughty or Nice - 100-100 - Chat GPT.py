def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []

    # Process commands from arguments
    for arg in args:
        command_parts = arg.split('-')
        counting_number = int(command_parts[0])
        name_list = [kid for kid in santa_list if kid[0] == counting_number]

        if len(name_list) == 1:
            if command_parts[1] == 'Nice':
                nice_list.append(name_list[0][1])
                santa_list.remove(name_list[0])
            elif command_parts[1] == 'Naughty':
                naughty_list.append(name_list[0][1])
                santa_list.remove(name_list[0])

    # Process commands from keyword arguments
    for name, category in kwargs.items():
        name_list = [kid for kid in santa_list if kid[1] == name]

        if len(name_list) == 1:
            if category == 'Nice':
                nice_list.append(name_list[0][1])
            elif category == 'Naughty':
                naughty_list.append(name_list[0][1])
            santa_list.remove(name_list[0])

    # Remaining kids are not found
    not_found_list = [kid[1] for kid in santa_list]

    # Output the results
    # output = []
    # if nice_list:
    #     output.append("Nice: {}".format(', '.join(nice_list)))
    # if naughty_list:
    #     output.append("Naughty: {}".format(', '.join(naughty_list)))
    # if not_found_list:
    #     output.append("Not found: {}".format(', '.join(not_found_list)))
    #
    # return '\n'.join(output)

    output = []
    if nice_list:
        output.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        output.append(f"Naughty: {', '.join(naughty_list)}")
    if not_found_list:
        output.append(f"Not found: {', '.join(not_found_list)}")

    return '\n'.join(output)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
