#Ask user to enter first name, middle initial and last name, 
#Concatinate them together and print out the result
First = input("Please enter your First Name: ")
MiddleInitial = input("Please enter your Middle Initial: ")
Last = input("Please enter your Last Name: ")

FullName = First + " " + MiddleInitial + " " + Last

print("Your full name is ", FullName)

print(f"Your full name is {First} {MiddleInitial} {Last}")

print("Your full name is %s %s %s" % (First, MiddleInitial, Last,))


