pin = 1234
if pin == 1234:
    print("Check Balance Deposit Money Withdraw Money Change PIN ")
amount = int(input("Enter the amount you have :"))
balance = 5000
balance1 = int(input("Enter the balance you have :"))
if amount > 0 :
    print("You have the sufficient balance")
else:
    print("You have insufficient balance")
if balance >= 100:
    print("You have sufficient balance")
else:
    print("You have insufficient balance")
deposit = int(input("Enter your balance :"))
if deposit < 0 :
    print("Your deposit is insufficient")
else:
    print("Your deposit added to balance")
    print(deposit + balance)
pin1 = int(input("What is your old pin :"))
if pin1 == pin :
    print("New pin cant match the curent pin")
    print("New pin must be 4 digits")
elif pin != pin1:
    print("Error")
elif pin != pin1:
    print("Access blocked")


    