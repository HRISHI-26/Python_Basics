        # Operator Overloading

class sample:
    def set_name(self, name):
        self.name = name

    # To change the function of  "+" operator
    def __add__(self, obj2):
        name = self.name+ " "+obj2.name
        return name
    
fname = sample()
lname = sample()

fname.set_name("Python")
lname.set_name("Tutorial")

# function of "+" replaced by __add__ constructor 
full_name = fname + lname
print("Full name: "+full_name)