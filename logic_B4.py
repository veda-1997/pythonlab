percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)
#output
#Enter percentage: 86
#Enter attendance %: 76
#Eligible for scholarship: False
