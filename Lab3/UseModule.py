# Program to test the use of the HandyMath Library

import HandyMath as HM

number1 = input("Enter first value:")
number2 = float(input("Enter second value:"))
number1 = float(number1)

mid = HM.midpoint(number1, number2)

print("The midpoint is: ", mid)

SR = HM.squareroot(number1)
print("The square root of the first value ia: ", SR)

EX = HM.exponent(number1, number2)
print("Number one raised to the power of number two is: ", EX)

MAX = HM.max(number1, number2)
print("The maximum values of the two values given is: ", MAX)

MIN = HM.min(number1, number2)
print("The Minimum value of the two numbers given is:", MIN)
