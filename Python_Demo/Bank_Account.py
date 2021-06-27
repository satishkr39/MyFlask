class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        print("Deposit in Account")
        self.balance = self.balance + deposit
        print("Balance is: {}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Amount can't exceed balance")
        else:
            print("Withdrawn Amount : {}".format(amount))
            self.balance = self.balance - amount
            print("Balance is: {}".format(self.balance))

    def __repr__(self):
        return f"The Person Name is : {self.name} and Balance is : {self.balance}"


p1 = Bank("satish", 1000)
print(p1)
p1.deposit(500)
p1.withdraw(100)
p1.withdraw(200)
print(p1)

