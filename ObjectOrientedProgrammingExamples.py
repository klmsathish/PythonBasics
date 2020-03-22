class Account():
    def __init__(self,balance):

        self.balance = balance
    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f"added{dep_amt}to the balance - now rs.{self.balance}")
    def withdrawl(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance = self.balance - wd_amt
            print("withdrawal accepted")
        else:
            print("sorry not enough funds!")
a = int(input("enter the number of bank accounts = "))

for b in range(a):
    j = int(input("enter deposit amount = "))
    m = int(input("enter withdrawal amount = "))
    k=j-m
    v=Account(k)
    v.deposit(j)
    v.withdrawl(m)

