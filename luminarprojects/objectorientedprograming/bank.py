import datetime
class Person:
    def setPerson(self,name,age):
        self.name=name
        self.age=age
    def printPerson(self):
        print(self.name,self.age)
class Bank(Person):
   bank_name="sdk"

   def createAccount(self,acno,balance):
       self.accountno=acno

       self.balance=3000

   def deposit(self,amount):
        self.balance+=amount
        print("your acc",Bank.bank_name,"has been credicted with amount of",amount,"aval amount is",self.balance)

   def withdraw(self,amount):
        self.balance-=amount

        if(amount>self.balance):
            print('insufficent balance in your acc')
        else:
            self.balance-=amount
            print("your acc", Bank.bank_name, "has been debited with amount of",amount, "on",datetime.date.today(),"aval amount is",self.balance)

   def balanceEnq(self):
        print("your acc balance is",self.balance)


obj=Bank()
obj.setPerson("r",27)
obj.printPerson()
obj.createAccount(1001,5000)
obj.deposit(10000)
obj.balanceEnq()
obj.withdraw(500)





