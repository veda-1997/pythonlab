dict1 = {"name": "Veda", "age": 19}
dict2 = {"branch": "CSE", "city": "Hyderabad"}

merged1 = dict1.copy()
merged1.update(dict2)

merged2 = dict1 | dict2

print("Using update():", merged1)
print("Using |:", merged2)

# Output:
# Using update(): {'name': 'Veda', 'age': 19, 'branch': 'CSE', 'city': 'Hyderabad'}
# Using |: {'name': 'Veda', 'age': 19, 'branch': 'CSE', 'city': 'Hyderabad'}
