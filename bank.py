class bank:
    def __init__(self):
        self.customer=""
        self.balance=0
    def details(self):
        self.name=input("enter the customer name")
        self.age=input("enter the custumer age")
        self.email=input("enter the customer email")
        self.address=input("enter the customer address")
        self.ph=input("enter the phone number")
    def deposit(self):
        self.amount=int(input("enter the amount deposited"))
        self.balance=self.balance+self.amount
        print("current amount",self.amount)
    def withdraw(self):
        self.wit=int(input("enter the withdrawal amount"))
        if(self.wit>=self.balance):
            print("balance is insufficient")
        else:
            self.balance=self.balance-self.wit
            print("now balance is",self.balance)
b=bank()
b.details()
b.deposit()
b.withdraw()
