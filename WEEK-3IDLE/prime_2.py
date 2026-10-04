lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for n in range(lower, upper + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
#OUTPUT
#Enter lower limit: 7
#Enter upper limit: 97
#7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
