def is_palindrome(word):
    return word == word[::-1]


words = ["madam", "hello", "level", "world", "radar"]

palindromes = list(filter(is_palindrome, words))

print("Palindromes:", palindromes)

# Output:
# Palindromes: ['madam', 'level', 'radar']
