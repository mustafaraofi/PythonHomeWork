# 7. Create a base class Shape with a method area. Create derived classes Square and Triangle that implement the area method.
class shape:
    def area():
        print("the shape you want should be square or triangle")
        
class square(shape):
    def __init__(self,one_side):
        self.one_side=one_side
    def area(self):
        a=self.one_side**2
        print(f"area of the square is {a}")
        
class triangle(shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        p=(self.a+self.b+self.c)/2
        A=(p*(p-self.a)*(p-self.b)*(p-self.c))**2
        print(f"area of the triangle is {A}")
        
squ=square(5)
squ.area()