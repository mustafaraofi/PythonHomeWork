#22. Create a class Log with methods to write error messages to a log file.
class Log:
    def __init__(self,log_file):
        self.log_file=log_file
    
    def write_error(self,message):
        with open(self.log_file,"a")as file:
            print(f"error:{message}\n")
            
l=Log("this is a file")
l.write_error("some thing was wrong")