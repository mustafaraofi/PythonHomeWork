#28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide methods to add and remove items from the menu.
class restaurant:
    def __init__(self,name):
        self.name=name
        self.menu=[]
        
    def add_items(self,items_name):
        self.menu.append(items_name)
        print("items added")
        
    def remove_items(self,items_name):
        if items_name in self.menu:
            self.menu.remove(items_name)
            print("the items removed")
        else:
            print("the items is not in restaurant")
            
