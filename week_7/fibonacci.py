def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter n:"))
print("The first 15 terms of the Fibonacci series:")
for i in range(1, n+1):
  print(fibonacci(i), end=" ")
#Enter n:15
#The first 15 terms of the Fibonacci series:
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 

  
      
    
