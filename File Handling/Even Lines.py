symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            # a = line.split()[::-1]
            result = ' '.join(line.split()[::-1])
            for symbol in symbols:
                result = result.replace(symbol, '@')
            print(result)
