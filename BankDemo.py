from datetime import datetime

class Bank:

    def openAccount(self,cname,balance,acno):
        self.cname=cname
        self.balance=balance
        self.acno=acno
        print("Hello ",self.cname,", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("Sorry You Need Another ",self.needs,"Rs.")
    def checkBalance(self):
        print("Current Balance : ",self.balance)

b1=Bank()
cname=input("Enter Customer Name : ")
balance=int(input("Enter InitialBalance : "))
acno=int(input("Enter Account Number : "))

b1.openAccount(cname,balance,acno)
file=open(str(acno)+".txt","w")

while True:

    print("****************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    print("****************************")
    choice=int(input("Enter Your Choice : "))
    print("****************************")

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("****************************")
        file.write("\nAmount Deposited : "+str(amount)+" On Time: "+str(datetime.now()))
        
    elif choice==2:
        amount=int(input("Enter Withdrawl Amount : "))
        b1.withdraw(amount)
        print("****************************")
        file.write("\nAmount Withdrawal : "+str(amount)+" On Time: "+str(datetime.now()))
    elif choice==3:
        b1.checkBalance()
        print("****************************")
        file.write("\nBalance Checked  On Time: "+str(datetime.now()))
    else:
        print("Thank You Using Our Services")
        print("****************************")
        file.write("\nTransaction Completed On Time: "+str(datetime.now()))
        break
file.close()
