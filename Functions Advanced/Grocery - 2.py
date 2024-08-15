def grocery_store(**products):
    sorted_products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    receipt = ''
    for product in sorted_products:
        receipt += f"{product[0]}: {product[1]}\n"
    return receipt[:-1]