student = {
    "name": "Veda",
    "age": 19,
    "branch": "CSE"
}

print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# Output:
# Keys:
# name
# age
# branch
# Values:
# Veda
# 19
# CSE
# Key-Value Pairs:
# name : Veda
# age : 19
# branch : CSE
