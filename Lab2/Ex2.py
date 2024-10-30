#Get the users birth year and subtract the current year 
#to get their current age.

birth_year = input("Please enter your four digit birth year")
birth_year = int(birth_year)

#This should be changed, we should not hard=code the year.
current_year = 2024

#This doesnt take into account the month, need to fix.
age = current_year - birth_year

print("You entered: ", birth_year)
print("Your age is:", age)