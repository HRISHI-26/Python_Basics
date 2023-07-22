# GLOBAL, NONLOCAL, LOCAL Variable scope

# global variable (scope) situated here
def check_scope():

        # Non local variable (scope) situated here
    
    def do_local():
                # Local variable (scope) situated here
        # "test" is local scope here
    
        test = "local test"

    def do_non_local():
        # nonlocal keyword converts "test" into nonlocal scope 
    
        nonlocal test
        test = "non local test"
    
    def do_global():
        # global keyword converts "test" into global scope
    
        global test
        test = "global test"

    test = "default"

    do_local()
    print("test value after do_local: "+test)
    
    do_non_local()
    print("Test value inside do_non_local: "+test)

    do_global()
    print("test value after do_global: "+test)

check_scope()

# "global test" is accessed from here due to global keyword inside "do_global" function
print("test value after do_global: "+test)