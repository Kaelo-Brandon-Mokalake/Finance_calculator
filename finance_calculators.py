import math

# A program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.

# getting user input
print("Choose either 'Investment' or 'Bond' from the menu below to proceed:")
print("\nInvestment\t- to calculate the amount of interest you will earn on interest \nBond\t\t- to calculate the amount you will have to pay on a home loan")
answer = input("Type in your answer: ").lower()

# user evaluation of which calculator to take and calculations
# if the user chooses the investment calculator
if answer == "investment":
    amount_deposited = float(input("Enter the amount of money you will like to deposit: "))
    interest_rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the number of years: "))
    interest = input("\nDo you want to go for simple or compound interest: ").lower()
# selecting Simple or Compound interest
    if interest == "simple":
        A = amount_deposited * (1 + (interest_rate / 100) * time)
        print("\nThe total amount invested is: R", round(A, 2))
    elif interest == "compound":
        A = amount_deposited * math.pow((1 + (interest_rate / 100)), time)
        print("\nThe total amount invested is: R", round(A, 2))
    else:
        print("\nInvalid entry. Please try again.")
# if the user chooses the bond calculator
elif answer == "bond":
    present_value = float(input("Enter the  present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    number_of_months = int(input("Enter the number of months you plan to take to repay the bond: ")) / 12
    x = ((interest_rate / 100) * present_value) / (1 - (1 + interest_rate)) ** (-number_of_months)
    print("\nThe money you will have to pay monthly is: R", round(x, 2))
else:
    print("\nInvalid entry. Please try again.")
