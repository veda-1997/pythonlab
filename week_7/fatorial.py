def recursive(n):
    if n<0 :
        print("invalid")
    if n==0 :
        return 1
    if n>0 :
        return n*recursive(n-1)


    
def iterative(n):
     if n<0 :
         print("invalid")
     result=1    
     for i in range(1,n+1):
         result *=i
     return result    
 
n=int(input("Enter n:"))
print("factorial of",n,"=",recursive(n))
print("factorial of",n,"=",iterative(n))
#Enter n:5
#factorial of 5 = 120
#factorial of 5 = 120
