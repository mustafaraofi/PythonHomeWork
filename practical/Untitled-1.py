# 1. Create a class called Person with attributes name and age. Create an object of the class and print its attributes.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def attributes(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        
        
ali=person(name="ali",age=23)
ali.attributes()


