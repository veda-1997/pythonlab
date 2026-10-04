n = int(input("Enter a number: "))

temp = n
sum = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    count += 1
    temp //= 10

average = sum / count

print("Sum =", sum)
print("Average =", average)

#OUTPUT
#Enter a number: 75649
#Sum = 31
#Average = 6.2
