#6. Create a base class Animal with a method speak. Create two derived classes Dog and Cat that override the speak method
class Animal:
    def speak():
        print("Animal can not speak")
        
class dag(Animal):
    def speak():
        print("dag is a dangerous animal")
        
class cat(Animal):
    def speak():
        print("the cat can eat buird")
        
rex=dag
rex.speak()
