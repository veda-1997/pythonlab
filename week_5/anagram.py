s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.lower().replace(" ", "")
s2 = s2.lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
#Enter first string: silent
#Enter second string: listen
#Anagrams
