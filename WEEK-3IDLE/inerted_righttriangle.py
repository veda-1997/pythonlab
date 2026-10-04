N = int(input("Enter number of rows: "))

for i in range(N, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# Enter number of rows: 5
# * * * * *
# * * * *
# * * *
# * *
# *
