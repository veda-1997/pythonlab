s = input("Enter a string: ")
sub = input("Enter substring: ")

find_index = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        find_index = i
        break

count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1

print("Find:", find_index)
print("Count:", count)

# Output:
# Enter a string: banana
# Enter substring: an
# Find: 1
# Count: 2
