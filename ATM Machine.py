import time

balance = int(500000)
pin = int(4268)

print("Welcome to the ATM!")
time.sleep(0.5)
print("What would you like to do today?")
time.sleep(0.5)
print("1. Check Balance")
time.sleep(0.5)
print("2. Withdraw Money")
time.sleep(0.5)
print("3. Deposit Money")
time.sleep(0.5)
print("4. Change PIN")
time.sleep(0.5)
print("5. Exit")
time.sleep(0.5)
choice = (input("Please enter your choice (1-5): ")).strip()


while True:
    if choice == "1":
        pinask = (input("Please enter your PIN: ")).strip()
    if pinask == pin:
        print("Your balance is:" , balance)
        break
    elif pinask != pin:
            print("Error, PIN is incorrect, please try again.")
            continue


while True:
    if choice == "2":
        pinask = (input("Please enter your PIN: ")).strip()
        if pinask == pin:
            withdrawal = input("How much would you like to withdraw?").strip()
        elif pinask != pin:
            print("Error, PIN is incorrect. Please try again.")
            continue
        try:
            withdrawal = float(withdrawal)
            print("Successful. Your new balance is:" , 'balance + withdrawal')
            break
        except ValueError:
            print("Error, please enter an integer or a decimal.")
            continue
        
        
while True:
    if choice == "3":
        pinask = input("Please enter your PIN: ").strip()
        if pinask == pin:
            deposit_amt = input("How much would you like to deposit?")
        elif pinask != pin:
            print("Error, PIN is incorrect. Please try again.")
        try:
            deposit_amt = float(deposit_amt)
            print("Successful, your new balance is now:" , balance + deposit_amt)
            break
        except ValueError:
            print("Please enter either an integer or a decimal")
            continue


while True:
    if choice == "4":
        pinask = input("Please enter your PIN: ").strip()
        if pinask == pin:
            newpin = input("Please enter your New PIN").strip()
            if newpin < 1000 or newpin > 9999:
                            print("Error. Please enter a 4-Digit integer")
                            continue
            try:
                newpin = int(newpin)
                print("Your pin has been succesfully changed. It is now: " , newpin)
                break
            except ValueError:
                print("Error, please enter a 4-Digit integer.")
                continue
            
if choice == "5":
    print("Thanks for visiting the ATM, Goodbye!")
    

while True:
    if choice not in ["1" , "2" , "3" , "4" , "5"]:
        print("Error, please enter 1, 2, 3, 4, or 5.")
        continue
    