student = {
    "name": "Veda",
    "age": 19,
    "branch": "CSE"
}

removed = student.pop("age")
print("Removed:", removed)

value = student.get("city", "Key not found")
print(value)

print(student)

# Output:
# Removed: 19
# Key not found
# {'name': 'Veda', 'branch': 'CSE'}
