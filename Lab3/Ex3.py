#Return the Suare root of the number 

def squareroot(n):
    return n ** 0.5

number = float(input("Enter a number to find its square root: "))
sr = squareroot(number)
print(f"The square root of {number} is {sr}")