            # ATM Project

def atm():
    
    PIN = 9775
    BALANCE = 1000
    MINI = []
    
    yes = 1
    pin = int(input("Enter your pin: "))

    while yes == 1:
        if pin == PIN:
            print("1.Deposit\n2.Withdrawal")
            print("3.Balance Checking\n4.Mini Statement")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                deposit = int(input("Enter amount to deposit: "))
                BALANCE += deposit
                MINI.append(deposit)
            elif choice == 2:
                withdraw = int(input("Enter amount to withdraw: "))
                if withdraw < BALANCE:
                    BALANCE -= withdraw
                    MINI.append(-abs(withdraw))
                else:
                    print("Limit exceeded!!!")
            elif choice == 3:
                print("Balance in account: " +str(BALANCE))
            elif choice == 4:
                print("Mini Statement: ",MINI)
            else:
                print("Incorrect option entered! ")
            yes = int(input("Do you want to continue(1/0): "))
            print("Thank you...")    
        else:
            print("Pin Incorrect !!!")
            pin = int(input("Enter your pin: "))  

atm()