#Name: Ryan Christopher
#Pawprint: rdcb2f
#Improved Object Position Calculator
#Module 3

#Equation: xf = x0 + v0t + 1/2at^2

#Functions
def doCalculation(x0, v0, a, t):
    answer = float(x0) + float(v0) * float(t) + 0.5 * float(a) * float(t) * float(t)
    print("xf =", float(x0), "+", float(v0), "*", float(t), "+ 0.5 *", float(a), "*", float(t), "*", float(t))
    print("xf =", float(x0), "+", float(v0), "*", float(t), "+ 0.5 *", float(a), "*", float(t) * float(t))
    print("xf =", float(x0), "+", float(v0) * float(t), "+", 0.5 * float(a) * float(t) * float(t))
    print("xf =", answer)
    print("\nFinal Answer:", answer, "Meters")

#Main Code
print("Welcome to the Object Postition Calcualtor")

repeat = True
# Checks if the user wants to make another calculation
while (repeat):
    print("Please enter the required information below\n")

    posHold = True
    # Makes sure user enters a float for initial position value
    while (posHold):
        try:
            iPosition = float(input("Initial Position (x0) = "))
        except ValueError:
            print("The value you entered is invalid. Please enter a numerical value.")
        else:
            posHold = False

    velHold = True
    # Makes sure user enters a float for initial velocity value
    while (velHold):
        try:
            iVelocity = float(input("Initial Velocity (v0) = "))
        except ValueError:
            print("The value you entered is invalid. Please enter a numerical value.")
        else:
            velHold = False
    
    accHold = True
    # Makes sure user enters a float for accleration value
    while (accHold):
        try:
            acceleration = float(input("Acceleration     (a)  = "))
        except ValueError:
            print("The value you entered is invalid. Please enter a numerical value.")
        else:
            accHold = False

    timeHold = True
    # Makes sure user enters a non-negative float for time value
    while (timeHold):
        try:
            time = float(input("Time             (t)  = "))
            if (time < 0):
                print("Negative elapsed times are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Please enter a numerical value.")
        else:
            timeHold = False

    print("\n")

    doCalculation(iPosition, iVelocity, acceleration, time)

    repeatVal = input("Would you like to perform another calculation? (y/n)\t")
    if (repeatVal == "y"):
        repeat = True
    else:
        repeat = False
        
print("Thank you for using the Object Position Calculator!")
