#19. Create a class Company with attributes name and employees (a list of Employee objects). Provide methods to add and remove employees.
class company:
    def __init__(self,name):
        self.name=name
        self.employees=[]
    
    def add_employees(self,employees_name):
        self.employees.append(employees_name)
        print("the employees added")
        
    def remove_employees(self,employees_name):
        if employees_name in self.employees:
            self.employees.remove(employees_name)
            print("the employees removed")
        else:
            print("this is not a employe in this company")
            
x=company("IBM")
x.add_employees("ahmad")
x.remove_employees("ahmad")


        