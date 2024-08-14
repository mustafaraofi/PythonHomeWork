#13. Create a class Laptop with private attributes brand, model, and price. Provide a method to apply a discount and a method to display laptop details.
class laptop:
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price
        
    def discount(self,discount_amount=10):
        d=(self.__price*discount_amount)/100
        print(f"your discount amount is {d}")
        x=self.__price - d
        print(f"and your payment is {x}")
        
    def laptop_details(self):
        print(f"the laptop brand is {self.__brand}")
        print(f"the laptop model is {self.__model}")
        print(f"the laptop price is {self.__price}")

lap=laptop(brand="dell",model="coray7",price=12000)
lap.laptop_details()
lap.discount()
        
        