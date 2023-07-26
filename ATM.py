# 26 - 7 - 2023  (Added To My Account GitHub)

# Object Of ATM

# Using getpass to hidden password
from getpass import getpass

# Message Welcome In Bank
print("Hello , Welcome To In QNB Bank ATM ")
print("----------------------")

# variables
restart = "Y"
balance = 20000
tries = 2

# part of password of card (Have 3 chance To Enter The Pass)
while tries >= 0:
    num_digit=int(getpass("please Enter Your Digit Number : "))     
    # Using the term between 999 to 10000 for user to enter 4 number just
    if num_digit < 10000 and num_digit > 999:
        while restart not in ("No" , "n" or "no" , "N" ) :
            
            # All Option In ATM
            dict_options = {
                1: "Your Balance",
                2: "To Withdraw",
                3: "To Pay In",
                4: "Return Card"
            }
            print("press 1 ==>" , dict_options[1])
            print("press 2 ==>" , dict_options[2])
            print("press 3 ==>" , dict_options[3])
            print("press 4 ==>" , dict_options[4])
            
            # Choose 1 , 2 , 3 , 4 Any Operation Are You Need
            option = int(input("Choose The Operation Are You Need "))
            
            # option one
            if option == 1 :
                print(f"Your Balance equal {balance}$")
                
                # To Do another operation
                restart = input("Would You Like To Back To Do Any Processing ")
                if restart in ("No" , "n" or "no" , "N" ):
                    print("Thanks And Withdraw The Card")
                    break
                else :
                    continue
            
            # option two
            elif option == 2:
                
                # Some Of Direct Chooses
                list_money =[50 , 100 , 200 , 500 , 1000 , 2000]
                print (list_money)
                
                # Using Direct Chooses
                need_choose = input("you need choose ? ")
                no_need = ("no" , "N" , "n" , "No" ) 
                if need_choose not in no_need :
                    options_money = int(input("Choose amount if you need "))
                    if options_money in list_money:
                        new_money = balance - options_money
                        print(f"The Balance is {new_money}$")
                        print("Take the card and the Cash")
                        break
                
                # Need To Withdraw Other amount
                else :
                    withdraw = int(input("please , Enter the amount you need Withdraw "))
                    restart = input("Sure Of Cash You Need ")
                    if withdraw <= balance and restart not in ("No" , "n" or "no" , "N" ):
                        new_balance = balance - withdraw
                        print(f"The Balance is {new_balance}$")
                        print("Take the card and the Cash")
                    else :
                        print("Please  , Sure your number of amount You Write")
                break
            
            # option three
            elif option == 3:
                pay_in = int(input("Enter The amount You Need Pay in & Sure Put The Money"))
                new_balance = balance + pay_in
                print(f"Your Balance is {new_balance}")
                print("Withdraw the card")
                break
            
            # option four 
            elif option == 4 :
                print("Withdraw the card")
                break
        break    
    tries = tries - 1
else:
    
    # Message After Using 3 chances  
    print("Please Withdraw The Card")
