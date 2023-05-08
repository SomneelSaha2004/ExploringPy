class Account:
    def __init__(self,name,balance):
        self.owner=name
        self.balance=balance
    def __str__(self)->str:
        return f"Account owner : {self.owner}\nAccount balance : {self.balance}"
    def deposit(self,amt):
        self.balance+=amt
        print("Deposit Accepted")
    def withdraw(self,amt):
        if(self.balance-amt<0):
            print("Funds Unavailible")
            return
        self.balance-=amt
        print("Withdrawal accepted")
        
