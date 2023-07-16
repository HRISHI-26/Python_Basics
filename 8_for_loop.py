# Program  for printing multiplication table

multiplicant = int(input("Enter an max multiplicant: "))
multiplier = int(input("Enter the multiplier: "))

for i in range(1,multiplicant+1):
    product = i * multiplier
    print(str(i)+"*"+str(multiplier)+"="+str(product))
    i = i + 1