a=int(input("Enter a year:"))
if a%4==0 and a%100 !=0 :
      print("given year is leap year")
elif a%400==0 :
    print("given year is a leap year")
else :
    print("given year is not a leap year")
      
#OUTPUT
#Enter a year:2020
#given year is leap year
    
