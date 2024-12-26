class BalenceExecption(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount,accName):
        self.balance=initialAmount
        self.name=accName
        print(f"\nAccount '{self.name}' created. \nBalance =${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")
    
    def deposite(self,amount):
        self.balance= self.balance+ (amount)
        print("\n Deposite complete.....")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalenceExecption(
                f"\n sorry, account '{self.name}' only has a balence of ${self.balance:.2f}"
            )  
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\n Withdraw Done !!")
            self.getBalance()
        except BalenceExecption as error:
            print(f"\n Withdraw inturrupted : {error}")

    def transfer(self,amount,account):
        try:
            print('\n\n*******beginning transfer...🎉')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\n transfer complete ...✅")
            print("\n\n ********* ")
        except BalenceExecption as error:
            print(f"\n Transfer Interrupted. ❌ {error}") 

class intereestRewardsAcct(BankAccount):
    def deposite(self,amount):
        self.balance=self.balance + (amount * 1.07)
        print("\n Deposite complete !!")
        self.getBalance()
 
class SavingAcct(intereestRewardsAcct):
    def __init__(self,initialAmont,acctName):
        super().__init__(initialAmont,acctName)
        self.fee=5

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\n withdraw done !!")
            self.getBalance()
        except BalenceExecption as error:
            print("\n Withdraw interrupt: {error}")

    
     

