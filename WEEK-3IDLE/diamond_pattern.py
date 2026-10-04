N = int(input("Enter N: "))

# Upper half
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end=" ")
        
    for j in range(2 * i - 1):
        print("*", end=" ")
        
    print()

# Lower half
for i in range(N, 0, -1):
    for j in range(N - i):
        print(" ", end=" ")
        
    for j in range(2 * i - 1):
        print("*", end=" ")
        
    print()

# Output:
# Enter N: 4
#       *
#     * * *
#   * * * * *
# * * * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *
