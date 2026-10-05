def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price

print("Only price:", calculate_price(1000))
print("Price and custom tax:", calculate_price(1000, 10))
print("All arguments:", calculate_price(1000, 10, 100))

# Output:
# Only price: 1180.0
# Price and custom tax: 1100.0
# All arguments: 1000.0
