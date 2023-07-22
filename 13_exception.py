        # Exception Handling 
try:
    dividend = int(input("Enter Dividend: "))
    divisor = int(input("Enter Divisor: "))
    quotient = dividend  / divisor
    print("Result: "+str(quotient))

except ZeroDivisionError:
    print("Division by zero not possible")

else:
    print("Try completed without Exception")

finally:
    print("Code Excecution completed")