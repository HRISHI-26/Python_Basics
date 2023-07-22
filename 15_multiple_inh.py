# MULTIPLE INHERITANCE & MRO POLICY

class First:
    def display(self):
        print("First")

class Second:
    def display(self):
        print("Second")

# Multiple Inheritance
    #  L1      L2   L3
class Third(First, Second):
    def display(self):
        print("Third")


t = Third()


# MRO POLICY 
print("Method Resolution Order: "+str(Third.mro()))
''' Call "display" if obtained from left_indexed_class (Priority L1->L2->L3)
     else go to next_indexed_class and find "display" method '''
t.display()