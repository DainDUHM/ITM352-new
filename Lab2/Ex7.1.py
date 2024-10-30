# ask the user to input a temp in degrees F.
# Convert that temp to C and output it.

#Function to convert degrees F to degrees C
def FtoC(temperatureF):
    degreesC = (float(degreesF) - 32) * (5/9)
    return(degreesC)

degreesF = input("Enter a temp in Fahrehheit")


print("This converts to ", FtoC(degreesF), " Celsius")