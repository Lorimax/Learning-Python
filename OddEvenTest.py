"""
This program requests a positive integer and tells if the number is odd or even.
"""
def printInfo():
    print("Odd or Even Test")

printInfo()
exit = False
while not exit:
    try:
        userInput = input("Please enter a positive integer number: ")
        userInput = int(userInput)
        if userInput <= 0:
            print("The number you have entered is not a positive number.")
            exit = False
        else:
            exit = True
    except:
        print("That is not a positive integer number.")
        exit = False
if userInput%2 > 0:
    print("The number is odd")
else:
    print("The number is even")
