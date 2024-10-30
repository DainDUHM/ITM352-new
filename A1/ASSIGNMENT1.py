import json
import random

# Load questions from a dictionary 
QUESTIONS = {
    "What is the air speed of an unladen swallow in miles/hr": ["12", "11", "8", "14"],
    "What is the capital of Texas": ["Austin", "San Antonio", "Dallas", "Houston"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"],
    "Which planet is known as the Red Planet": ["Mars", "Venus", "Jupiter", "Saturn"],
    "What is the largest ocean on Earth": ["Pacific", "Atlantic", "Indian", "Arctic"],
    "Who wrote 'To Kill a Mockingbird'": ["Harper Lee", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"],
    "What is the square root of 64": ["8", "6", "7", "9"],
    "Which element has the chemical symbol 'O'": ["Oxygen", "Osmium", "Gold", "Silver"],
    "Who developed the theory of relativity": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
    "Which country is the largest by area": ["Russia", "Canada", "China", "United States"],
    "What is the smallest prime number": ["2", "1", "3", "5"],
    "Who was the first President of the United States": ["George Washington", "Thomas Jefferson", "John Adams", "Benjamin Franklin"],
    "Which year did the Titanic sink": ["1912", "1905", "1920", "1918"],
    "What is the chemical symbol for water": ["H2O", "O2", "CO2", "NaCl"],
    "What is the longest river in the world": ["Nile", "Amazon", "Yangtze", "Mississippi"]
}

# Function to get a valid user answer
def get_user_answer():
    while True:
        answer = input("Your answer (a-d): ").lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        print("Invalid response. Please enter a valid option (a-d).")

# Function to run the quiz
def run_quiz(questions):
    score = 0
    high_score = 0

    # Load the previous high score if it exists
    try:
        with open('high_scores.txt', 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        pass

    for question, alternatives in questions.items():
        correct_answer = alternatives[0]
        shuffled_alternatives = random.sample(alternatives, len(alternatives))

        # Display the question and options
        print(f"\n{question}")
        for label, alternative in zip(['a', 'b', 'c', 'd'], shuffled_alternatives):
            print(f"{label}) {alternative}")

        # Get the user's answer
        user_answer = get_user_answer()
        answer = shuffled_alternatives[ord(user_answer) - ord('a')]

        # Check if the answer is correct
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer!r}, not {answer!r}")

    # Display final score
    print(f"\nYour final score is {score}/{len(questions)}")

    # Write the score to a history file
    with open('score_history.txt', 'a') as file:
        file.write(f"Score: {score}/{len(questions)}\n")

    # Check if the user has a new high score
    if score > high_score:
        print("Congratulations! You've got a new high score!")
        with open('high_scores.txt', 'w') as file:
            file.write(str(score))
    else:
        print(f"Your high score remains: {high_score}")

# Main function to run the quiz app
def main():
    run_quiz(QUESTIONS)

if __name__ == "__main__":
    main()