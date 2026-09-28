import re

def check_password(pw):
    failed = []

    if len(pw) < 8:
        failed.append("At least 8 characters")

    if not re.search(r'[A-Z]', pw):
        failed.append("At least one uppercase letter")

    if not re.search(r'[a-z]', pw):
        failed.append("At least one lowercase letter")

    if not re.search(r'\d', pw):
        failed.append("At least one digit")

    if not re.search(r'[!@#$%^&*]', pw):
        failed.append("At least one symbol from !@#$%^&*")

    return failed

password = "Veda123"
print(check_password(password))

# Output:
# ['At least 8 characters', 'At least one symbol from !@#$%^&*']
