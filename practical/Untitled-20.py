#20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods to add and remove animals
class Zoo:
    def __init__(self,name):
        self.name=name
        self.animals=[]
    
    def add_animals(self,animals_name):
        self.animals.append(animals_name)
        print("the animals added")
        
    def remove_animals(self,animals_name):
        if animals_name in self.animals:
            self.animals.remove(animals_name)
            print("the animals removed")
        else:
            print("this animal is not in Zoo")
            
c=Zoo("kabul zoo")
c.add_animals("lion")
c.remove_animals("lion")

        