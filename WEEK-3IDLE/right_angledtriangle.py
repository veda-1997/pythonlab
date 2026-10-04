N = int(input("Enter number of rows: "))

for i in range(1, N + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# Enter number of rows: 5
# *
# * *
# * * *
# * * * *
# * * * * *
