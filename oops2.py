class bank:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    def debit(self,amount):
        self.balance=self.balance-amount
        print("Debited account", self.balance)
    def credit(self,amount):
        self.balance=self.balance+amount
        print("Credited account",self.balance)
    def rest_balance(self):
        return self.balance

s1=bank(2345,451561)
s1.debit(245)
s1.credit(10000)