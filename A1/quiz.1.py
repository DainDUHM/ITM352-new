# First version of the quiz game

answer = input('What is the airspeed of an unladen swallow in miles/hr?')

if answer == '12':
    print("correct!")
else:
    print(f"The answer is '12', not {answer!r}")

answer = input("What is the capitol of Texas?")
if answer =="Austin":
    print("Correct!")
else:
    print(f"The answer is 'Austin', not {answer!r}")