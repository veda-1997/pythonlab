students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]

sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Students:", sorted_students)

names = ["Veda", "Meghana", "Aarav", "Sai"]

sorted_names = sorted(names, key=lambda x: len(x))
print("Names:", sorted_names)

# Output:
# Students: [('Sita', 92), ('Ravi', 78), ('Amit', 65)]
# Names: ['Veda', 'Sai', 'Aarav', 'Meghana']
