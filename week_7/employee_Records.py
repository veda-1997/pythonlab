from functools import reduce

employees = [
    {"name": "meghana", "department": "IT", "salary": 50000},
    {"name": "vasantha", "department": "HR", "salary": 40000},
    {"name": "akhila", "department": "IT", "salary": 60000},
    {"name": "Dharani", "department": "Sales", "salary": 45000}
]

# Select employees from IT department
it_employees = filter(lambda emp: emp["department"] == "IT", employees)

# Give selected employees a 10% salary hike
hiked_employees = map(
    lambda emp: {**emp, "salary": emp["salary"] * 1.10},
    it_employees
)

# Convert to list
result = list(hiked_employees)

# Calculate total salary using reduce()
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    result,
    0
)

print("Employees after 10% hike:")
for emp in result:
    print(emp)

print("Total salary expenditure:", total_salary)

