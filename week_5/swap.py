s = input("Enter string: ")

result = ""

for i in s:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i

print("Swapped case:", result)
#Enter string: HeLlo
#Swapped case: hElLO
