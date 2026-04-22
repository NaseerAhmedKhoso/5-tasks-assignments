class BankAccount:
    owner=""
    balance=""

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def depositamount(self):
        print(self.owner,"Deposited PKR ",self.balance ,"|","New balance : PKR",self.balance)

acco1=BankAccount("Naseer Ahmed",300000)
acco2=BankAccount("Ali",700000)
acco3=BankAccount("Farooque",120000)
acco4=BankAccount("Hussnain",50000)

acco1.depositamount()
acco2.depositamount()
acco3.depositamount()
acco4.depositamount()