class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("your balance isnt enought : Charngin a 5$ fee" )
            self.balance -= 5
    def display_account_info(self):
        print("Balance : {}".format(self.balance))
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

Nicole = BankAccount( 0.08, 0)
Luiza = BankAccount(0.06, 0)
Nicole.deposit(100)
Nicole.deposit(250)
Nicole.deposit(300)
Nicole.withdraw(155)
Nicole.yield_interest()
Nicole.display_account_info()
# print(Nicole.balance)
Luiza.deposit(300)
Luiza.deposit(855)
Luiza.withdraw(100)
Luiza.withdraw(150)
Luiza.withdraw(300)
Luiza.withdraw(50)
Luiza.yield_interest()
Luiza.display_account_info()
# print(Luiza.balance)

@classmethod
def get_all_accounts(cls):
    for i in cls.accounts:
        i.display_account_info()