#Append user spcified value to a tuple


Weird = ("hello", 10, "goodbye", 3, "goodnight", 5, "Go away")


userVal = ("Please enter a value ")


try:
   Weird.append(userVal)
except:
   print("You cannot add elements to a tuple doofus!")
