#Name: Ryan Christopher
#Pawprint: rdcb2f
#Object Position Calculator
#Module 2

#Equation: xf=x0+v0t+1/2at^2

#Functions
def doCalculation(x0, v0, a, t):
    answer = float(x0) + float(v0) * float(t) + 0.5 * float(a) * float(t) * float(t)
    print("xf =", float(x0), "+", float(v0), "*", float(t), "+ 0.5 *", float(a), "*", float(t), "*", float(t))
    print("xf =", float(x0), "+", float(v0), "*", float(t), "+ 0.5 *", float(a), "*", float(t) * float(t))
    print("xf =", float(x0), "+", float(v0) * float(t), "+", 0.5 * float(a) * float(t) * float(t))
    print("xf =", answer)
    print("\nFinal Answer:", answer, "Meters")

#Main Code
print("Welcome to the Object Position Calculator")
print("Please enter the required information below\n")
    
iPosition = input("Initial Position (x0) = ")
iVelocity = input("Initial Velocity (v0) = ")
acceleration = input("Acceleration     (a)  = ")
time = input("Time             (t)  = ")

print("\n")

doCalculation(iPosition, iVelocity, acceleration, time)

print("\nThank you for using the Object Position Calculator")


