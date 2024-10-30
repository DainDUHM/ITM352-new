#Create the list of responses from Exercise 3.3 (values 5, 7, 3, 8)
#Next add the response “0” to the end of the list using the 
#.append() method. Next add the response “6” to the list between the values 7 and 3

responseValues = [5, 7, 3, 8, 0]
responseValues.append(0)
#responseValues.insert(2,6)

responseValues = responseValues[0:2] + [6] + responseValues[2:]
responseValues.sort()
responseValues.remove(0)

print(responseValues)