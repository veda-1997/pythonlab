from functools import reduce

words = ["Python", "is", "very", "easy"]

sentence = reduce(lambda a, b: a + " " + b, words)

print(sentence)

# Output:
# Python is very easy
