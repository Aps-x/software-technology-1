## Author: Adam Seaton
## Date created: 23/03/2023
## Date last changed: 23/03/2023
## This program prompts the user to input a coefficient of restitution of a ball and an initial height in meters.
## The program then calculates the number of times the ball bounces and the total distance traveled before it rises
## to a height of less than 10cm.
## Input: none, Output: none

# Variables
restitutionCoefficient = 0
initialHeight = 0
# Constants
MIN_HEIGHT = 0.1

# Functions
def main():
    printMenu()
    calculateBouncesAndDistance()
    tryAgain()

def printMenu():
    global restitutionCoefficient
    global initialHeight
    # Retrieve user input
    restitutionCoefficient = float(input("Enter coefficient of restitution: "))
    initialHeight = float(input("Enter initial height in meters: "))


def calculateBouncesAndDistance():
    global restitutionCoefficient
    global initialHeight
    # Variables
    height = initialHeight
    bounces = 0
    totalDistance = 0
    # Loop
    while height >= MIN_HEIGHT:
        totalDistance += height * 2
        height *= restitutionCoefficient
        bounces += 1
    # Display results
    print(f"Number of bounces: {bounces}")
    print(f"Meters traveled: {round(totalDistance - initialHeight, 2)}")


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
                print("==================================")
                main()
            elif data == 'n':
                exit()
            break


main()