#create funtion called midpoint and takes 2 numbers ans input
#and returns the halfway value

def midpoint(num1, num2):
    return ((num1 + num2)/2)

number1 = input("Enter first value:")
number2 = float(input("Enter second value:"))

number1 = float(number1)

mid = midpoint(number1, number2)

print("The midpoint is: ", mid)