text = "hello"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)

# Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
