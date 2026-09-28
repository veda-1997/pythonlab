numbers = (10, 20, 30)

try:
    numbers[1] = 50
except TypeError as e:
    print("Error:", e)

# Output:
# Error: 'tuple' object does not support item assignment
