# solution 1:
# def grocery_store(**kwargs):
#     sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#
#     result = []
#     for k, v in sorted_products:
#         result.append(f"{k}: {v}")
#
#     return '\n'.join(result)

# solution 2:
# def grocery_store(**products):
#     sorted_products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     receipt = ''
#     for product in sorted_products:
#         receipt += f"{product[0]}: {product[1]}\n"
#     return receipt[:-1]

# solution 3:
def grocery_store(**kwargs):
    sorted_result = [f'{key}: {value}' for key, value in
                     sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return '\n'.join(sorted_result)

# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

