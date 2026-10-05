balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited:", amount)
    print("Current balance:", balance)


def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        print("Amount withdrawn:", amount)
        print("Current balance:", balance)
    else:
        print("Insufficient funds!")


while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == 3:
        print("Current balance:", balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

 #--- Bank Menu ---
#1. Deposit
#2. Withdraw
#3. Check Balance
#4. Exit
#Enter your choice: 1
#Enter deposit amount: 7000
#Amount deposited: 7000.0
#Current balance: 8000.0
       
