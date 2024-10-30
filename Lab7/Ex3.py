
# Examine every elements print out messages ect.. weird tuple


Weird = ("hello", 10, "goodbye", 3, "goodnight", 5)
numStrings = 0


for x in Weird:
   if (type(x) is str):
       numStrings += 1


print(f"We have {numStrings} strings")
