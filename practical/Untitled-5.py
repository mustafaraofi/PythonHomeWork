#5. Create a class Rectangle with methods to compute the area and perimeter. Initialize the class with the length and width.
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def the_rectangle_area(self):
        A=self.length*self.width
        print(f"the rectangle area is {A}")
        
    def the_rectangle_perimeter(self):
        p=2*(self.length+self.width)
        print(f"the rectangle perimeter is {p}")
        

rec1=rectangle(length=8,width=12)
rec1.the_rectangle_area()
rec1.the_rectangle_perimeter()