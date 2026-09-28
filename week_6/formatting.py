import re

text = "Important dates are 28/09/2026 and 15/08/2025."

pattern = r'(\d{2})/(\d{2})/(\d{4})'

dates = re.findall(pattern, text)
print("Dates:", dates)

result = re.sub(pattern, r'\3-\2-\1', text)
print(result)

# Output:
# Dates: [('28', '09', '2026'), ('15', '08', '2025')]
# Important dates are 2026-09-28 and 2025-08-15.
