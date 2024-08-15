from collections import deque

words = ["rose", "tulip", "lotus", "daffodil"]

vowels = deque([chr for chr in input().split()])
consonants = deque([chr for chr in input().split()])

is_find_word = False

last_collected_word = None
collected_word = set()
while not is_find_word and vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        if vowel in word:
            collected_word.add(vowel)

        if consonant in word:
            collected_word.add(consonant)

        if all(chrr in collected_word for chrr in word):
            last_collected_word = word
            is_find_word = True
            break

if is_find_word:
    print(f"Word found: {last_collected_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

