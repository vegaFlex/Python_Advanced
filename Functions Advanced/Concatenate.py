# def concatenate(*args, **kwargs):
#     concatenate = ''
#     for word in args:
#         concatenate += word
#
#     for key, value in kwargs.items():
#         if key in concatenate:
#             concatenate = concatenate.replace(key, value)
#
#     return concatenate

def concatenate(*args, **kwargs):
    result = "".join(args)
    for key, value in kwargs.items():
        result = result.replace(key, value)
    return result

# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

