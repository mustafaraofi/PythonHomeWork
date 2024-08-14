#14. Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw, and check the balance.
class bankaccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print("deposit completed")
        else:
            print("some thing was wrong")
    
    def withdraw(self,amount):
        if 0<amount<self.__balance:
            self.__balance -= amount
            print("withdraw completed")
        else:
            print("some thing was wrong")
            
    def check_the_balance(self):
        print(f"your balance is {self.__balance}")
        
ahmad = bankaccount(account_number=7654321,balance=200000)
ahmad.deposit(10000)
ahmad.withdraw(20000)
ahmad.check_the_balance()
        
        