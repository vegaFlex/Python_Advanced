import os

try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')

# correct:
# if os.path.exists('my_first_file.txt'):
#     os.remove("my_first_file.txt")
# else:
#     print('File already deleted!')