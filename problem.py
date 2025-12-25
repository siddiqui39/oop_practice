
class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("BDT", amount, "was debited")
        print("Total balance= ",self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("BDT", amount, "was credited")
        print("Total balance= ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(150)
acc1.credit(500)
acc1.debit(4000)
acc1.credit(2500)
acc1.debit(22)
acc1.credit(378)