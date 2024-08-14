#17. Create a class School with attributes name and students (a list of Student objects). Provide methods to add and remove students
class school:
    def __init__(self,name):
        self.name=name
        self.students=[]
        
    def add_student(self,student_name):
        self.students.append(student_name)
        print("student added")
            
    def remove_student(self,student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print("student removed")
        else:
            print("the student is not in school")
            
marf=school("marf")
marf.add_student("ahmad")
marf.remove_student("ahmad")

        