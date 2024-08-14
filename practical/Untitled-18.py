#18. Create a class Team with attributes name and members (a list of Person objects). Provide methods to add and remove members.
class team:
    def __init__(self,name):
        self.name=name
        self.members=[]
    
    def add_members(self,member_name):
        self.members.append(member_name)
        print("the member added")
        
    def remove_members(self,member_name):
        if member_name in self.members:
            self.members.remove(member_name)
            print("the member removed")
        else:
            print("this is not a member in this team")
            
crickt=team("crickt")
crickt.add_members("ali")
crickt.remove_members("ali")

        