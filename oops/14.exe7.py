'''Encapsulation - Protecting Attributes: Implement a class Account with a private attribute balance and provide methods to deposit and withdraw safely, 
checking for sufficient funds.'''

class Account:
    def __init__(self, balance=0):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposit amount is:{amount}, New balance is:{self.__balance}")

    def withdraw(self,amount):
        self.__balance-=amount
        print(f"withdraw amount is :{amount},your balance is {self.__balance}")  
    def balance(self):
        print(f"your acc balance is :{self.__balance}")      

acc=Account(100)
acc.deposit(200)
acc.balance()