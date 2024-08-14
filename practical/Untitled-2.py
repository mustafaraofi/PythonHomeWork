# Add a method called greet to the Person class that prints a greeting message including the person's name 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def attribites(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")

    def greeting(self,greeting_message):
        print(greeting_message)
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
ahmad=person(name="Ahmad",age=45)
ahmad.greeting("Hello how are you?")