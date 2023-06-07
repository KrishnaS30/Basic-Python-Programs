#This program performs as finance calculators: an investment calculator or home loan repayment calculator

#Importing necessary python libraries 
import math

#The following code helps user to choose between 'investment' or 'bond'
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
option=input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#The below code converts the selected option to all lowercase letters
option=option.lower()

#The following blocks of code checks the user selection option and performs the calculations or outputs error message according to the option

if option == 'investment':
    #For investment calculator, the below commands gets the principal amount, rate of interest, number of years and also user option to select 'simple' or 'compound' interest
    principal_amount=float(input("Enter the amount to deposit: "))
    rate_of_interest=float(input("Enter the interest rate(in percentage): "))
    years=int(input("Enter the number of years for investment: "))
    interest=input("Enter the type of interest - 'simple' or 'compound' : ")
    
    #The below commands, divides the rate of interest by 100 and converts the interest option to all lowercase letters
    rate_of_interest=rate_of_interest/100.0
    interest=interest.lower()
    #The below commands calculates total amount based on the interest option and displays the corresponding message or the value
    if interest== 'simple':
        total_amount=principal_amount*(1+rate_of_interest*years)
    elif interest== 'compound':
        total_amount=principal_amount* math.pow((1+rate_of_interest),years)
    else:
        print("You have entered an invalid interest option")
    print("The total amount once " + interest + " interest is applied: " + str(total_amount))
     
elif option == 'bond':
    #For home loan repayment calculator, the below commands gets the present value of house, rate of interest and number of months
    present_house_value=float(input("Enter the present value of house: "))
    interest_rate=float(input("Enter the interest rate(in percentage): "))
    months=int(input("Enter the number of months : "))

    #The below code calculates the monthly interest rate, the repayment amount and displays the repayment amount
    monthly_interest_rate=(interest_rate/100.0)/12.0
    repayment=(monthly_interest_rate*present_house_value)/(1-(1+monthly_interest_rate)**(-months))
    print("The total amount user will have to repay is " + str(repayment))   
else:
    print("You have entered an invalid option")    