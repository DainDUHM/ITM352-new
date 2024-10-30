#Interactive quize game with questions and answers in a list 

QUESTIONS = [
    ("What is the air speed of an unladen swallow in miles/hr", "12"),
    ("What is the Capitol of Texas", "Austin"), 
    ("The Last Supper was painted by which artist", "Da Vinci"),
    ("Who won Superbowl XXXIV", "Rams")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")