from functools import reduce

numbers = [10, 25, 7, 40, 15]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum:", maximum)

# Output:
# Maximum: 40
