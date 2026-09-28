s = input("Enter a string: ")
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev = rev + s[i]

print("Reversed string:", rev)
#Enter a string: meghana
#Reversed string: anahgem

s = input("Enter a string: ")
print("Reversed string:", s[::-1])
#Enter a string: veda
#Reversed string: adev
#Enter a string: meghana
#Reversed string: anahgem
