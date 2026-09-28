s = input("Enter string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for i in s:
    if i == old:
        result += new
    else:
        result += i

#print("Result:", result)
#Enter string: meghana
#Enter character to replace: e
#Enter new character: a
#Result: maghana
