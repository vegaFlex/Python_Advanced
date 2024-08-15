# def age_assignment(*args, **kwargs):
#     result = {}
#
#     for name in args:
#         first_letter = name[0]
#         if first_letter in kwargs:
#             result[name] = kwargs[first_letter]
#
#
#     result_2 = []
#     for k, v in result.items():
#         result_2.append(f"{k} is {v} years old.")
#
#     return '\n'.join(result_2)

# def age_assignment(*args, **kwargs):
#     result = {}
#
#     for name in args:
#         first_letter = name[0]
#         age = kwargs[first_letter]
#         result[name] = age
#
#     sorted_result = [f"{name} is {age} years old." for name, age in
#                      sorted(result.items(), key=lambda x: x[0])]
#
#     return '\n'.join(sorted_result)

# def age_assignment(*names, **ages):
#     result = []
#     for name in names:
#         age = ages.get(name[0], None)
#         if age is not None:
#             result.append(f"{name} is {age} years old.")
#     return '\n'.join(sorted(result))

def age_assignment(*names, **ages):
    result = []
    for name in names:
        age = ages.get(name[0])
        result.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
