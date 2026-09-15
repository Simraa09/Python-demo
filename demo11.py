balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Balance:", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited successfully")
        print("New balance:", balance)

    case 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    case 4:
        print("Thank you for using the ATM")

    case _:
        print("Invalid choice")