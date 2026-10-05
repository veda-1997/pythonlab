square = lambda x: x * x
check_even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b

print("Square:", square(5))
print("Even:", check_even(8))
print("Larger:", larger(10, 7))

# Output:
# Square: 25
# Even: True
# Larger: 10
