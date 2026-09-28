data = ("Veda", [10, 20, 30])

data[1].append(40)

print(data)

# Output:
# ('Veda', [10, 20, 30, 40])

# The tuple itself is immutable, but the nested list is mutable.
# Therefore, the contents of the list can be modified.
