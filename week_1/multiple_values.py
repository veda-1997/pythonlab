values = input("Enter numbers separated by spaces: ")

numbers = values.split()
numbers = [int(x) for x in numbers]

total = sum(numbers)

print("Sum:", total)

# Output:
# Enter numbers separated by spaces: 10 20 30
# Sum: 60
