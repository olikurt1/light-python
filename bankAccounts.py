class BankAccount:
    def __init__(self, AccountName, OwnerName, Balance):
        self.OwnerName = OwnerName
        self.Balance = Balance
        self.AccountName = AccountName

    def __repr__(self):
        return f"Bank Account Name= {self.AccountName}\nOwnerName= {self.OwnerName}\nBalance= {self.Balance}"
    
    def deposit(self, n):
        self.Balance += n
    
    def withdraw(self, n):
        if n > self.Balance:
            return "Balance is too low"
        else:
            self.Balance -= n

class SavingsAccount(BankAccount):
    def __init__(self, AccountName, OwnerName, Balance, Interest):
        super().__init__(AccountName, OwnerName, Balance)
        self.Interest = Interest

    def __repr__(self):
        return f"{super().__repr__()}\nInterest= {self.Interest}"

    def applyInterest(self):
        self.Balance += self.Balance*self.Interest

acc = BankAccount("Current Account", "Oliver", 200)
acc.deposit(50)
acc.withdraw(300)
print(acc)

savings = SavingsAccount("Savings Account", "Oliver", 20000, 0.05)
print(savings)
savings.applyInterest()
print(savings)
