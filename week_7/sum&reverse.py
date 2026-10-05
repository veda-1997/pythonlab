def sum_of_digits(n):
   if n==0 :
       return 0
   else :
      return (n % 10) + sum_of_digits(n // 10)
n=int(input("Enter n:"))
print("sum of digits of ",n,"=",sum_of_digits(n))      
