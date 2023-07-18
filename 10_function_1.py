                # FUNCTION

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modules")

                # FUNCTION DEFINITION
def calculator():
    choice = int(input("Enter your choice: "))
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    if choice == 1:
        result = number_1 + number_2
        print("Result: "+str(result))
    elif choice == 2:
        if number_1 > number_2:
            result = number_1 - number_2
        else:
            result = number_2 - number_1
        print("Result: "+str(result))
    elif choice == 3:
        result = number_1 * number_2
        print(result)
    elif choice == 4:
        if number_1 > number_2:
            result = number_1 / number_2
            print(result)
        else:
            print("Input Invalid")
    elif choice == 5:
        if number_1 > number_2:
            result = number_1 % number_2
            print(result)
        else:
            print("Invalid Input")
            # FUNCTION CALL
calculator()