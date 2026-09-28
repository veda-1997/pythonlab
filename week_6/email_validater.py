import re

def is_valid_email(s):
    pattern = r'^[\w.]+@[\w.-]+\.[A-Za-z]{2,6}$'
    return bool(re.fullmatch(pattern, s))

valid_emails = [
    "veda@gmail.com",
    "meghana123@yahoo.in",
    "hello.world@company.org",
    "student_1@college.edu"
]

invalid_emails = [
    "a@b.c",
    "no-at-sign.com",
    "veda@gmail",
    "@gmail.com"
]

for email in valid_emails:
    print(email, ":", is_valid_email(email))

for email in invalid_emails:
    print(email, ":", is_valid_email(email))

# Output:
# veda@gmail.com : True
# meghana123@yahoo.in : True
# hello.world@company.org : True
# student_1@college.edu : True
# a@b.c : False
# no-at-sign.com : False
# veda@gmail : False
# @gmail.com : False
