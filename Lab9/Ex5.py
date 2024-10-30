import json


file_path = 'quiz_questions.json'


with open(file_path, 'r') as json_file:
    questions = json.load(json_file)

    
    for question, alternatives in questions.items():
        print(f"Question: {question}")
        for alternative in alternatives:
            print(f"  - {alternative}")
        print()