s = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for i in s:
    if i == ch:
        count += 1

print("Occurrences:", count)
#Enter string: meghana
#Enter character: a
#Occurrences: 2
