#8. Create a class Employee with attributes name and salary. Create a derived class Manager with an additional attribute department.
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def showinfo(self):
        print(self.name)
        print(self.salary)
        
class manger(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def showinfo(self):
        print(self.name)
        print(self.salary)
        print(self.department)
        
a=manger(name="ahmad",salary=200000,department="IT")
a.showinfo()