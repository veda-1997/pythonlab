s = input("Enter an identifier: ")

if s and (s[0].isalpha() or s[0] == "_"):
    valid = True
    for ch in s[1:]:
        if not (ch.isalnum() or ch == "_"):
            valid = False
            break
else:
    valid = False

if valid:
    print("Valid identifier")
else:
    print("Invalid identifier")

# Output:
# Enter an identifier: student_name1
# Valid identifier
