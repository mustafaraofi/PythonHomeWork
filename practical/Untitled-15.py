#15. Create a class Student with private attributes name, grade, and age. Provide methods to get and set these attributes and a method to display the student's details.
class student:
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age
        
    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade
    def get_age(self,age):
        if self.age>0:
            return self.age
        else:
            print("age is fales")
    def students_details(self):
        print(f"student name is {self.name}")
        print(f"student grade is {self.grade}")
        print(f"student age is {self.age}")
ahmad=student(name="ahmed",grade=12,age=20)
ahmad.students_details()