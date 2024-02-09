"""
This program allows users to access two
different financial calculators:
- Investment calculator
- Home loan repayment calculator

Program start asking user to choose between investment or bond.
If user choose investment, the program will ask for the:
-	Deposit money amount.
-	The interest rate.
-	Number of years of investment.
-	Type of investment (simple or compound).
The program will calculate the final amount that user going to 
have after the given number of years and output the answer.

If user choose bond, the program will ask for the:
-	The present value of the house.
-	The interest rate.
-	The number of the months they plan to take to repay the bond.
The program will calculate how much money the user will 
have to repay each month and output the answer.

If user choose something different from investment and 
bond, the program will give and error message. 
"""

import math

print("investment - to calculate the amount",
       "of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#save the user input or choice
user_input = input("Enter either 'investment' or 'bond' to proceed: ") 

#when user select Bond Option
if user_input.lower() == "bond":

    #Variables to store user inputs
    h_value = float(input("Enter the present value of the house: "))
    b_interest_rate = (float(input("Enter the interest rate: ")) / 100)/12
    months = int(input("Enter the number of months to repay the bond: "))
    repayment = (b_interest_rate*h_value)/(1-(1+b_interest_rate)**(-months))

    #The bond output
    print("------------------------------------------")
    print(f"Present House Value: {h_value}")
    print("Monthly Interest Rate: "+format(b_interest_rate,".4f"))
    print(f"Number of Months to Repay the Bond: {months}")
    print(f"Monthly Repayment value: "+format(repayment,".2f"))
    print("------------------------------------------")

#when user select the Investment Option
elif user_input.lower() == "investment":

    #variables to store user inputs
    deposit_money = float(input("Enter the deposit money amount: "))
    in_interest_rate = float(input("Enter the interest rate: ")) / 100
    years = int(input("Enter the number of years: "))
    interest = input("Enter either 'simple' or 'compound' interest: ")

    #Compound Option IF
    if interest.lower() == "compound":
        #calculation when user choose compound investment option
        total_amount = deposit_money*math.pow((1+in_interest_rate),years)

    #Simple Option IF
    elif interest.lower() == "simple":
        #calculation when user choose simple investment option
        total_amount = deposit_money*(1+in_interest_rate*years)

    #The investment Output
    print("------------------------------------------")
    print(f"Deposit Money amount: {deposit_money}")
    print(f"Interest Rate: "+format(in_interest_rate,".2f"))
    print(f"Number of Years: {years}")
    print(f"Interest: {interest}")
    print(f"Total amount: "+format(total_amount,".2f"))
    print("------------------------------------------")
else:
    #Error message when user choose different from investment or bond
    print("ERROR - Wrong Option, try again with the correct Option!!")
