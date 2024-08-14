#21. Create a class FileManager with methods to read from and write to a file.
class file_manager:
    def __init__(self,file_adress):
        self.file_adress=file_adress
        
    def read(self):
        with open(self.file_adress , "r") as file:
            print(file)
            
    def write(self):
        with open(self.file_adress , "w") as file:
            print(file)
            
            
f=file_manager('D\Hurmatullah\New folder\n.txt')
f.read()

        