# Return the max of two numbers given

def max_value(num1, num2):
    return num1 if num1 > num2 else num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = max_value(num1, num2)
print(f"The larger value is: {result}")