# SOLUTION 1:

# def palindrome(word, idx):
#     if idx >= len(word) // 2:
#         return f'{word} is a palindrome'
#
#     left = word[idx]
#     rigth = word[-1 - idx]
#
#     if left != rigth:
#         return f'{word} is not a palindrome'
#
#     return palindrome(word, idx + 1)


# SOLUTION 2:

def palindrome(word, index=0):

    # Base case: if index is greater than or equal to the middle of the word, the word is a palindrome
    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    # Recursive case: compare the characters at the beginning and end of the word
    if word[index] != word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"

    # Recursive case: move the index one position to the right and call the function recursively
    return palindrome(word, index + 1)

print(palindrome("abcba", 0))
# print(palindrome("peter", 0))