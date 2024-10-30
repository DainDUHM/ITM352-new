#Interactive quiz game where each question has four possible answers
#MAKE QUESTIONS a dictionary 
#Allow user to select the correct answer by its label.

QUESTIONS = {
    "What is the air speed of an unladen swallow in miles/hr": ["12", "11", "8", "14"],
    "What is the Capitol of Texas": ["Austin", "San Antonio", "Dallas", "Houston"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alernatives = sorted(alternatives)
    for label, alternatives in enumerate(sorted_alernatives):
        print(f"{label}: {alternatives}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alernatives[answer_label]

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}")