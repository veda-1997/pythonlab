def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)

print("For n = 3:")
tower_of_hanoi(3, "A", "B", "C")
print("Total moves:", 2**3 - 1)

print("\nFor n = 4:")
tower_of_hanoi(4, "A", "B", "C")
print("Total moves:", 2**4 - 1)

# Output:
# For n = 3:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
# Total moves: 7
#
# For n = 4:
# Move disk 1 from A to B
# Move disk 2 from A to C
# Move disk 1 from B to C
# Move disk 3 from A to B
# Move disk 1 from C to A
# Move disk 2 from C to B
# Move disk 1 from A to B
# Move disk 4 from A to C
# Move disk 1 from B to C
# Move disk 2 from B to A
# Move disk 1 from C to A
# Move disk 3 from B to C
# Move disk 1 from A to B
# Move disk 2 from A to C
# Move disk 1 from B to C
# Total moves: 15
