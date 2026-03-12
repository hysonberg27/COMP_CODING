bal = 100000000000000
amt = int(input("Enter amount to withdraw: "))

if amt > 0:
    if amt <= bal:
        bal = bal - amt
        print("Withdrawal successful")
        print("Remaining balance:", bal)
    else:
        print("Insufficient balance")
else:
    print("Invalid amount")
