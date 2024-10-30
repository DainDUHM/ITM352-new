import json


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


file_path = 'quiz_questions.json'
with open(file_path, 'w') as json_file:
    json.dump(QUESTIONS, json_file, indent=4)

print(f"Questions have been saved to {file_path}")