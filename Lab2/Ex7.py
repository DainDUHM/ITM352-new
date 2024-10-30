# ask the user to input a temp in degrees F.
# Convert that temp to C and output it.

degreesF = input("Enter a temp in Fahrehheit")

degreesC = (float(degreesF) - 32) * (5/9)

print("This converts to ", degreesC, " Celsius")
