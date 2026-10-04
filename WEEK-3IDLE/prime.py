n = int(input("Enter a number: "))

if n < 2:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
#OUTPUT
#Enter a number: 7
#Prime Number
        
