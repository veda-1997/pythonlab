items = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

highest = max(items, key=items.get)
lowest = min(items, key=items.get)

print("Highest:", highest, items[highest])
print("Lowest:", lowest, items[lowest])

# Output:
# Highest: Laptop 55000
# Lowest: Mouse 800
