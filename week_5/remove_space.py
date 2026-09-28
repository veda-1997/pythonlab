s = input("Enter string: ")

result = ""

for i in s:
    if i != " ":
        result += i

print("String without whitespace:", result)
#Enter string: unity in diversity
#String without whitespace: unityindiversity
