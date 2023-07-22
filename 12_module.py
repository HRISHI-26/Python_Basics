    # This is an example for module 
#  Here we import the module sample_eg which was made to show this example

# inside this file
print(__name__)

import sample_eg as eg

# Inside module imported
print(__name__)
num = int(input("Enter your number: "))
eg.check(num)

newcheck = eg.check
newcheck(num )

# from mod_name import func_name