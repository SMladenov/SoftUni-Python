#Online Banking

class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = [int(i) for i in input().split(', ')]

cmd = input()

while cmd != "End":
    cmdSplit = cmd.split('#')
    action = cmdSplit[0]
    if action == "Send Money":
        money = int(cmdSplit[1])
        pinCode = int(cmdSplit[2])
        try:
            if money > balance:
                raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
            if pinCode != pin:
                raise PINCodeError("Invalid PIN code")
            if age < 18:
                raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

            balance -= money
            print (f"Successfully sent {money:.2f} money to a friend")
            print (f"There is {balance:.2f} money left in the bank account")
        
        except (MoneyNotEnoughError, PINCodeError, UnderageTransactionError) as e:
            print (e)
    elif action == "Receive Money":
        money = int(cmdSplit[1])
        try:
            if money < 0:
                raise MoneyIsNegativeError("The amount of money cannot be a negative number")
            balance += (money / 2)
            print (f"{(money / 2):.2f} money went straight into the bank account")
        
        except MoneyIsNegativeError as e:
            print (e)
    cmd = input()
