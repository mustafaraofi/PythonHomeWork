#10. Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override the fly method in Penguin to indicate that penguins cannot fly.
class Bird:
    def fly():
        print("Birds can flying!")
    
    class eagle(bird):
        def fly():
            print("The eagle flying very high!")

    class penguin(bird):
        def fly():
            print("Penguins can not flying.")

f=eagle
f.fly()