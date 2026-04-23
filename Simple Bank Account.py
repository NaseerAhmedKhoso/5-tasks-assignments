class BankAccount:
    owner=""
    balance=""

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(self.owner," You have Deposited PKR ",amount,"|","New balance : PKR",self.balance)

    def withdraw(self,amount):
        self.balance-=amount
        if amount<=self.balance:
            print( self.owner,"You have withdrawed : PKR",amount," | Your new balance :PKR",self.balance)
        else:
            print("You have insufficint balance")

    
print(" Wellcome to ATM Machine")
print("\n")
print("1 : Deposit")

print("2 : Withdraw")

choice=int(input("Enter Your Choice :"))
if choice==1:
    print("1 : Naseer")
    print("2 : Ali")
    print("3 : Farooque")
    print("4 : Hussnain")
    choice=int(input("Enter your choice : "))
    if choice==1:
        Naseer=BankAccount("Naseer Ahmed",3000)
        Naseer.deposit(int(input("Enter your amount : ")))
    elif choice==2:
        Ali=BankAccount("Ali",7000)
        Ali.deposit(int(input("Enter your amount : ")))
    elif choice==3:
        Farooque=BankAccount("Farooque",1200)
        Farooque.deposit(int(input("Enter your amount : ")))
    elif choice==4:
        Hussnain=BankAccount("Hussnain",500)
        Hussnain.deposit(int(input("Enter your amount : ")))
    
    
elif choice==2:
    print("1 : Naseer")
    print("2 : Ali")
    print("3 : Farooque")
    print("4 : Hussnain")
    choice=int(input("Enter your choice"))
    if choice==1:
        Naseer=BankAccount("Naseer Ahmed",3000)
        Naseer.withdraw(int(input("Enter your amount : ")))
    elif choice==2:
        Ali=BankAccount("Ali",7000)
        Ali.withdraw(int(input("Enter your amount : ")))
    elif choice==3:
        Farooque=BankAccount("Farooque",1200)
        Farooque.withdraw(int(input("Enter your amount : ")))
    elif choice==4:
        Hussnain=BankAccount("Hussnain",500)
        Hussnain.withdraw(int(input("Enter your amount : ")))
