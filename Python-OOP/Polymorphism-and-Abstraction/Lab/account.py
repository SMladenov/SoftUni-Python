class Account:
    def __init__ (self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: list = []
        

    @property
    def balance (self):
        return self.amount + sum(self._transactions)
  
    def handle_transaction (self, transaction_amount):  
        if transaction_amount <= 0:
            if self.balance - transaction_amount < 0:
                raise ValueError("sorry cannot go in debt!")
            else:
                self._transactions.append(transaction_amount)
                return f"New balance: {self.balance}"
        else:
            self._transactions.append(transaction_amount)
            return f"New balance: {self.balance}"
    
    def add_transaction (self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            self.handle_transaction(amount)
        
        
    def __str__ (self):
        return f"Account of {self.owner} with starting amount: {self.amount}"
    
    def __repr__ (self):
        return f"Account({self.owner}, {self.amount})"
    
    def __len__ (self):
        return len(self._transactions)
    
    def __iter__ (self):
        return iter(self._transactions)

    def __getitem__ (self, index):
        if 0 <= index < len(self._transactions):
            return self._transactions[index]

    def __reversed__ (self):
        return reversed(self._transactions)
    
    def __eq__ (self, account):
        if isinstance(account, Account):
            return self.balance == account.balance
    
    def __ne__ (self, account):
        if isinstance(account, Account):
            return self.balance != account.balance
    
    def __ge__ (self, account):
        if isinstance(account, Account):
            return self.balance >= account.balance
    
    def __le__ (self, account):
        if isinstance(account, Account):
            return self.balance <= account.balance
    
    def __gt__ (self, account):
        if isinstance(account, Account):
            return self.balance > account.balance
        
    def __lt__ (self, account):
        if isinstance(account, Account):
            return self.balance < account.balance
    
    def __add__ (self, account):
        if isinstance(account, Account):
            name = f"{self.owner}&{account.owner}"
            balance = self.amount + account.amount
            newAccount = Account(name, balance)
            newAccount._transactions = self._transactions + account._transactions
            return newAccount

acc = Account('bob', 10)

acc2 = Account('john')

print(acc)

print(repr(acc))

acc.add_transaction(20)

acc.add_transaction(-20)

acc.add_transaction(30)

print(acc.balance)

print(len(acc))

for transaction in acc:

    print(transaction)

print(acc[1])

print(list(reversed(acc)))

acc2.add_transaction(10)

acc2.add_transaction(60)

print(acc > acc2)

print(acc >= acc2)

print(acc < acc2)

print(acc <= acc2)

print(acc == acc2)

print(acc != acc2)

acc3 = acc + acc2

print(acc3)

print(acc3._transactions)