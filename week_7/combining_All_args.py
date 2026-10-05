def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)

    print("Items:")
    for item in items:
        print("-", item)

    print("Discount:", discount, "%")

    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").title() + ":", value)

order_summary(
    "Meghana",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)

# Output:
# Customer: Meghana
# Items:
# - Laptop
# - Mouse
# Discount: 10 %
# Extra Information:
# Delivery Address: Hyderabad
# Gift Wrap: True
