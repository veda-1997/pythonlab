s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
#OUTPUT
#Enter a string: ab cd e5
#Vowels = 2
#Consonants = 3
#Digits = 1
#Spaces = 2

