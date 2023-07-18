                # FUNCTION

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modules")

choice = int(input("Enter your choice: "))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

                # FUNCTION DEFINITION
def calculator(number_1, number_2):
    if choice == 1:
        result = number_1 + number_2
        return result
    elif choice == 2:
        if number_1 > number_2:
            result = number_1 - number_2
        else:
            result = number_2 - number_2
        return result
    elif choice == 3:
        result = number_1 * number_2
    elif choice == 4:
        if number_1 > number_2:
            result = number_1 / number_2
            return result
        else:
            result = "Input Invalid"
            return result
    elif choice == 5:
        if number_1 > number_2:
            result = number_1 % number_2
            return result
        else:
            result = "Input Invalid"
            return result
            

            # FUNCTION CALL
result = calculator(number_1, number_2)
if choice == 4 or choice == 5:
    print(result)
else:
    print("Result: "+str(result))
