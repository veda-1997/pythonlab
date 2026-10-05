numbers = [1, 2, 3, 4, 5, 6, 9]

cubes = list(map(lambda x: x ** 3, numbers))
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Cubes:", cubes)
print("Divisible by 3:", divisible_by_3)

# Output:
# Cubes: [1, 8, 27, 64, 125, 216, 729]
# Divisible by 3: [3, 6, 9]
