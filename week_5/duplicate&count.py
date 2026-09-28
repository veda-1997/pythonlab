s = input("Enter a string: ")

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in count:
    if count[ch] > 1:
        print(ch, ":", count[ch])

# Output:
# Enter a string: programming
# r : 2
# g : 2
# m : 2
