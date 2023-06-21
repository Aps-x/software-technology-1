## Author: Adam Seaton
## Date created: 23/03/2023
## Date last changed: 23/03/2023
## This program requests the face value, interest rate, current market price, and years until maturity of a bond
## and then calculates its yield to maturity. It will also prompt the user if they want to try again or exit.
## Input: none, Output: none

# Variables
faceValue = 0
interestRate = 0
currentMarketPrice = 0
yearsUntilMaturity = 0

# Functions
def main():
    printMenu()
    calculateBondYield()
    tryAgain()


def printMenu():
    global faceValue
    global interestRate
    global currentMarketPrice
    global yearsUntilMaturity
    # Retrieve user input
    faceValue = float(input("Enter face value of bond: "))
    interestRate = float(input("Enter coupon interest rate: "))
    currentMarketPrice = float(input("Enter current market price: "))
    yearsUntilMaturity = float(input("Enter years until maturity: "))


def calculateBondYield():
    # Calculate bond yield
    interest = interestRate * faceValue
    a = (faceValue - currentMarketPrice) / yearsUntilMaturity
    b = (faceValue + currentMarketPrice) / 2
    yieldToMaturity = ((interest + a) / b) * 100
    # Print result
    print(f"Approximate YTM: {round(yieldToMaturity, 2)}%")


def tryAgain():
    while True:
        # Ask the user if they wish to try again
        print("Do you want to try again? y/n")
        data = input()
        # Input validation
        if data.lower() not in ('y', 'n'):
            print("Please enter either 'y' or 'n'")
        # Try again if 'y', exit if 'n'
        else:
            if data == 'y':
                print("============================")
                main()
            elif data == 'n':
                exit()
            break


main()