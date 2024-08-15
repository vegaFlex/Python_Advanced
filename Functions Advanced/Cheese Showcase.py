def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    # variant 1
    for cheese, pieces in sorted_cheeses:
        result.append(cheese)

        pieces.sort(reverse=True)
        result.extend(pieces)


    # variant 2
    # for cheese, pieces in sorted_cheeses:
    #     pieces.sort(reverse=True)
    #
    # for k, v in sorted_cheeses:
    #     result.append(k)
    #     result.extend(v)


    # variant 3
    # for key, value in sorted_cheeses:
    #     result.append(key)
    #     result += sorted(value, reverse=True)

    return '\n'.join([str(x) for x in result])


# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )

# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
