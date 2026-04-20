balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))
acc_type = int(input("Enter account type (1-Savings, 2-Current): "))

if amount > 50000:
    print("EXCEEDS MAXIMUM LIMIT")

elif amount % 100 != 0:
    print("NOT A MULTIPLE OF 100")

elif acc_type == 1:   # Savings
    if balance - amount < 500:
        print("INSUFFICIENT BALANCE")
    else:
        print("SUCCESS")
        print("New balance =", balance - amount)

elif acc_type == 2:   # Current
    fee = 50 if amount > 25000 else 0

    if balance < amount + fee:
        print("INSUFFICIENT BALANCE")
    else:
        print("SUCCESS")
        print("New balance =", balance - amount - fee)

else:
    print("Invalid account type")