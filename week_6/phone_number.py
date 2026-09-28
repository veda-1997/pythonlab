import re

text = "Call 555-123-4567, (555) 123-4567 or 555.123.4567."

pattern = r'\(?(\d{3})\)?[-.\s]+(\d{3})[-.\s]+(\d{4})'
numbers = re.findall(pattern, text)

for number in numbers:
    phone = "-".join(number)
    print(phone)

# Output:
# 555-123-4567
# 555-123-4567
# 555-123-4567
