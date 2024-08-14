# 3. Create a class called Car with attributes make, model, and year. Include a method to print out the car's details. 
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
         
    def car_details(self):
        print(f"the car made by {self.make}")
        print(f"the car model is {self.model}")
        print(f"the car made in {self.year} year")
        
car1=car(make="toyota",model="hailax",year=2018)
car1.car_details()
        
