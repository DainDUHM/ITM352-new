# Ask the user to enter an arbitrary sentance. 
#Calculate the length of the string and return that value.

sentence = input("enter a sentence: ")

stringLength = len(sentence)
outputString = "You entered \"" + sentence + "\". It has a length of " + str(stringLength)
print(outputString)