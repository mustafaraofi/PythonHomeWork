#9. Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that override the drive method.
class vehicle:
    def drive():
        print("every vehicle has a driver")
        
class bike(vehicle):
    def drive():
        print("the bicycle has two tires")
        
class turck(vehicle):
    def drive():
        print("every turck has more then 4 tires")
        
d=turck
d.drive()