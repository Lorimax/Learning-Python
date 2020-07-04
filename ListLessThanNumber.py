"""
This program filters a list of positive integers for numbers less than a previously defined number.
"""

numbers = []
filterNumber = 0

def printInfo():
    print("""
    This program filters a list of positive integers for numbers less than a previously defined number.
    ===================================================================================================""")

def isPositiveInteger(numberToCheck):
    try:
        numberToCheck = int(numberToCheck)
        if numberToCheck < 0:
            print(str(numberToCheck) + " is not a positive integer")
            return False
        else:
            return True
    except:
        print(str(numberToCheck) + " is not a positive integer")
        return False

def getUserInput(numbers):
    global filterNumber
    filterNumber = input("Please enter the number you want to filter by: ")
    while not isPositiveInteger(filterNumber):
        filterNumber = input("Please enter the number you want to filter by: ")
    print("""Please enter all the numbers you want to filter. Please press 'Enter' after each number.
To filter the numbers enter 'filter'.""")
    exit = False
    while not exit:
        userInput = input("Number: ")
        if userInput == "filter":
            exit = True
        elif isPositiveInteger(userInput):
            numbers.append(userInput)

def calculateLessThanFilterNumber(numbers, filterNumber):
    resultNumbers = []
    if isPositiveInteger(filterNumber):
        for number in numbers:
            if isPositiveInteger(number) and int(number) < int(filterNumber):
                    resultNumbers.append(number)
    return resultNumbers


printInfo()
getUserInput(numbers)
print("Numbers less than " + str(filterNumber) + ":")
print(calculateLessThanFilterNumber(numbers, filterNumber))
