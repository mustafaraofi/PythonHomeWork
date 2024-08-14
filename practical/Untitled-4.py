#4. Create a class Circle with a method to compute the area. Initialize the class with the radius.
from math import pi
class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def circle_area(self):
        x=pi*self.radius**2
        print(f"the circle area is {x}")
        
        
        
cir=circle(radius=12)
cir.circle_area()