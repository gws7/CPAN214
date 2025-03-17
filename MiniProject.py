# Mini Project
CORRECT_PIN = 1010
attempts = 3
balance = 1500

def displayBalance():
    print(f"Balance: {balance:.2f}")

def withdrawalValidation(amount):
    global balance
    if amount < 0:
        print("Invalid Amount")
    elif amount > balance:
        print("Cannot withdraw more than total balance")
    else:
        balance -= amount
        print(f"Current Balance: {balance:.2f}")     

def withdrawal():
    global balance
    amount = 0
    print("""
          1. Withdraw 20 dollars
          2. Withdraw 40 dollars
          3. Withdraw 60 dollars
          4. Withdraw 80 dollars
          5. Withdraw 100 dollars
          6. Withdraw custom amount
          """)
    withdrawalAmount = int(input("Enter Withdrawal Choice: "))
    match withdrawalAmount:
        case 1:
            amount = 20
        case 2:
            amount = 40
        case 3:
            amount = 60
        case 4:
            amount = 80
        case 5:
            amount = 100
        case 6:
            amount = float(input(f"Enter custom amount. Your current balance is {balance}. "))
        case _:
            print("Invalid Entry")
            return
    
    withdrawalValidation(amount)
    
def deposit():
    global balance
    depositAmount = float(input(f"Enter deposit amount: "))
    balance += depositAmount
    print(f"Your new balance is {balance:.2f}")
    
def exitProgram():
    print("Exiting Program")
    exit()

# Keeps checking as long as user has attempts valid
while attempts > 0:
    pin = int(input("Enter the 4 digit pin: "))
    if (pin == CORRECT_PIN):
        print("Correct Pin Entered")
        # If its right the loop breaks and since attempt != 0 then it will proceed to the menu
        break  
    else:
        attempts -= 1
        # If its wrong, -1 is subtracted from the attempts total
        print("Invalid Pin")

# If attempts reach 0, program exits
if(attempts == 0):
    print("Too many failed attempts. Exiting...")
else:
    while True:
        choice = int(input("What would you like to do?\n1 - Display Balance\n2 - Make a withdrawal\n3 - Make a deposit\n4 - Exit the program\n"))
        # Switch statement to work with different cases
        match choice:
            case 1:
                displayBalance()
            case 2:
                withdrawal()
            case 3:
                deposit()
            case 4:
                exitProgram()
            case _:
                print("Invalid Choice")