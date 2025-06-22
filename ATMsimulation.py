balance = 10000 # balance of 10k
password = "1234"

# three functions of withdraw, deposit, check balance 
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposit successful. Current balance:", balance)

def check_balance():
    print("Current balance:", balance)

# password authentication with maximum 3 attempts 
for attempt in range(3):
    entered_password = input("Enter your password: ")
    if entered_password == password:
        print("Password accepted.\n")
        break
    else:
        print("Incorrect password. Try again.")

else:
    print("You have exceeded the maximum number of attempts. Goodbye!")
    exit()

# menu in a loop 
while True:
    print("\nWelcome to ATM")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = int(input("Enter the amount to withdraw: "))
        withdraw(amt)
    elif choice == 2:
        amt = int(input("Enter the amount to deposit: "))
        deposit(amt)
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
