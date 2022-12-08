print ("""********
Welcome to the Automatic Teller Machine (ATM) System
    
Process;
    
1. Review your account balance
    
2. Deposit money
    
3. Withdraw money

4. Exit to press red button("q" == red button)
    
********""")

Balance = 10000

while True:
    process = input("Select the process you want to do: ")
    
    if (process == "q"):
        print("Thank you for using our ATM system. Have a nice day!")
        break
    elif (process == "1"):
        print("Your balance is $", Balance)
        
    elif (process == "2"):
        amount = int(input("How much money do you want to deposit? "))
        Balance += amount
        
    elif (process == "3"):
        
        amount = int(input("How much money do you want to withdraw? "))
        
        if(Balance-amount < 0):
            print("You don't have enough money in your account!")
            continue
        
        Balance -= amount
    
    else:
        print("Invalid process")
    


