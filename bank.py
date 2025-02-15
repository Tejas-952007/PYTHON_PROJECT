# Function to check the account balance
def balance(money):
    print(f"Your current balance is: {money}")
    return money

# Function to make a payment
def pay(money):
    payment = int(input("Enter the amount to pay: "))
    money += payment
    print(f"Your new balance after payment is: {money}")
    return money

# Function to withdraw money
def withdraw(money):
    receive = int(input("Enter the amount to withdraw: "))
    if receive > money:
        print("Insufficient funds!")
    else:
        money -= receive
        print(f"Your new balance after withdrawal is: {money}")
    return money

# Initial balance
money = 100000

# Heading of the bank
print("\n <--$$ DUMMY BANK $$-->")

# Enter pin number
pin = input("Enter the code: ")

# Check if the pin is correct
if pin == "1234@bank":
    print(f" <--:--> Welcome sir, dummy bank account name Tejas:--")
    while True:
        print(f"\nChoose the number->\n1. Check account balance\n2. Pay\n3. Withdraw\n4. Exit")
        choice = int(input("Enter the number:--->> "))
        if choice == 1:
            money = balance(money)
        elif choice == 2:
            money = pay(money)
        elif choice == 3:
            money = withdraw(money)
        elif choice == 4:
            print("Thank you for using Dummy Bank. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
else:
    print("Invalid input.")