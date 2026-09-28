s = input("Enter a sentence: ")

words = s.split()
result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i] + " "

print(result)
#Enter a sentence: meghana is a good girl
#girl good a is meghana 
