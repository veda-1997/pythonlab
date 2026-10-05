items = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

sorted_items = sorted(items.items(), key=lambda x: x[1])

for item, price in sorted_items:
    print(item, ":", price)

# Output:
# Mouse : 800
# Keyboard : 1500
# Monitor : 12000
# Laptop : 55000
