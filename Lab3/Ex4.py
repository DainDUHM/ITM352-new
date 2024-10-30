# Return the exponent
def exponent(base, exp):
    return base ** exp

base = float(input("Enter the base: "))
exp = float(input("Enter the exponent: "))
result = exponent(base, exp)
print(f"{base} raised to the power of {exp} is {result}")