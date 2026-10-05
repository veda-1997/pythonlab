def to_upper(word):
    return word.upper()


words = ["hello", "python", "world"]

result = list(map(to_upper, words))

print("Original:", words)
print("Uppercase:", result)

# Output:
# Original: ['hello', 'python', 'world']
# Uppercase: ['HELLO', 'PYTHON', 'WORLD']
