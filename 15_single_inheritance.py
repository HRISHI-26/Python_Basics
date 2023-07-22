# OOPS Concepts
# Single Inheritance is used

class BaseClass:

    # This is a Constructor
# Constructor automatically Excecutes when Object is Instantiated

    def __init__(self):
        print("This is Base Class")
    

# " set_name & display " are 2 methods
    def set_name(self, name):
        self.name = name
        print("set_name completed")
    

    def display(self):
        print("Name: "+self.name)



        # Here SubClass is Inheriting BaseClass
class SubClass(BaseClass):

# Constructor automatically Excecutes when Object is Instantiated
    # Constructor overriding is done

    def __init__(self):
        print("This is Sub Class")
    

    def display_name(self):
        print("Redirecting to super class")

        # super() used to call method from Base Class
        super().set_name("SUB CLASS")
        super().display()
    
    # Method Overring is done here
    def display(self):
        print("This method is Overrided.")

# Creating Object for Base Class
base = BaseClass()

# Calling its own methods
base.set_name("OOPs!!!")
base.display()


# Creating Object for Sub Class
sub = SubClass()
# Calling method in Base Class using object of Sub Class
sub.set_name("Python")

# Calling method of Sub Class itself
sub.display_name()

# Calling display function in Sub Class
sub.display()