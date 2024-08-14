#11. Create a class Account with private attributes balance. Provide public methods to deposit and withdraw money
class accont:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"your new balance is {self.__balance}")
            
    def withdraw(self,amount):
        if 0<amount<self.__balance:
            self.__balance -= amount
            print(f"your new balance is {self.__balance}")
        else:
            print("you can not withdraw this amount!")
            
Ahmad=accont(1200)
Ahmad.deposit(500)

