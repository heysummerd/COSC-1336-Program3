#---------------------
# Summer Davis
# COSC 1336
# Project 3
#---------------------
# Objective
# This program will compute and display the bank's fees for the month
# based on how many checks the customer has deposited
#
# The program will ask users for the current month and how many
# checks were deposited during that month.
#
# The bank charges a fixed fee of $10 per month.
# In addition, the bank charges the following fees for a checking account:
# $.10 each for fewer than 20 checks
# $.08 each for 20-39 checks
# $.06 each for 40-59 checks
# $.04 each for 60 or more checks
#
# The program will display an error message for any negative inputs
#---------------------

# Named constants
MONTHLY_FEE = 10

# This function displays the start of the project
def header ():
    print('\nBank Teller\'s Entry')
    print('-' * 80)
    
def main():
    # Header of the project
    header()

    # Get movie name and ticket count
    month = input('Enter the month ')
    checks = getIntegerEntry('Enter the number of checks written this month? ')

    # Validate input
    while checks < 0:
        print('Cannot enter a negative number')
        checks = getIntegerEntry('Enter the number of checks written this month? ')

    # Calculate fees
    total = MONTHLY_FEE + calculateFees(checks)

    # Display fee summary
    feeSummary(month, checks, total)
    
    # End of project display
    footer()

# This function will calculate the fees
def calculateFees(checks):
    if checks < 20:
        return checks * 0.10
    elif checks < 39:
        return checks * 0.08
    elif checks < 59:
        return checks * 0.06
    else:
        return checks * 0.04

# This function will display the Fee Summary
def feeSummary(month, checks, total):
    print('\n' + '-' * 80)
    print('Check Fees Summary')
    print('-' * 80)
    print(f'    Month of statement: {month}')
    print(f'    For writing {checks} checks, the bank fee is ${total:,.2f}')
    print('\n')


# This function will get users entry of float data
def getFloatEntry(prompt):
    value = float(input(prompt))
    return value

# This function will get users entry of integer data
def getIntegerEntry(prompt): 
    value = int(input(prompt))
    return value
    
# This function displays the end of the project
def footer():
    print('-' * 80)
    print('End of Project 3')
    
main()
