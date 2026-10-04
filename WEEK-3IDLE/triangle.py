a=float(input("enter the first side of the triangle :"))
b=float(input("enter the second side of the triangle :"))
c=float(input("enter the third side of the triangle:"))
if a+b>c and b+c>a and c+a>b :
        if a==b and b==c :
           print("given triangle is an equilateral triangle")
        elif a==b:
           print("given triangle is an isosceles triangle")
        else:
           print("given triangle is a scalene triangle")
else :
    print("given triangle is invalid")
    
#OUTPUT:
#enter the first side of the triangle :7
#enter the second side of the triangle :9
#enter the third side of the triangle:18
#given triangle is invalid    


#enter the first side of the triangle :7
#enter the second side of the triangle :7
#enter the third side of the triangle:5
#given triangle is an isosceles triangle
