N = int(input("Enter N: "))

# Upper half
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Lower half
for i in range(N - 1, 0, -1):
    for j in range(N - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Output:
# Enter N: 4
#       *
#     *   *
#   *       *
# *           *
#   *       *
#     *   *
#       *
