n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number =", reverse)

#OUTPUT
#Enter a number: 6547
#Reversed number = 7456
