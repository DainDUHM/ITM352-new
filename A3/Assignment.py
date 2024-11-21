from flask import Flask, render_template, request, redirect, url_for, session
import json
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load questions from JSON file
def load_questions():
    with open('questions.json', 'r') as file:
        return json.load(file)

# Route to the home page, which shows the quiz
@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    questions = load_questions()
    random.shuffle(questions)
    session['questions'] = questions
    session['current_question'] = 0
    session['score'] = 0

    return render_template('index.html', question=questions[0])

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

# Route to handle answer submissions
@app.route('/answer', methods=['POST'])
def answer():
    user_answer = request.form['answer']
    question_index = session.get('current_question', 0)
    questions = session.get('questions', [])
    
    if question_index < len(questions):
        correct_answer = questions[question_index]['correct']
        if user_answer == correct_answer:
            session['score'] += 1

        session['current_question'] = question_index + 1
        if session['current_question'] < len(questions):
            return render_template('index.html', question=questions[session['current_question']])
        else:
            return redirect(url_for('result'))

# Route to display the result
@app.route('/result')
def result():
    score = session.get('score', 0)
    username = session.get('username', 'Guest')

    # Load leaderboard
    try:
        with open('leaderboard.json', 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    # Add current score to leaderboard
    leaderboard.append({'username': username, 'score': score})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]

    # Save updated leaderboard
    with open('leaderboard.json', 'w') as file:
        json.dump(leaderboard, file)

    return render_template('result.html', score=score, leaderboard=leaderboard)

if __name__ == "__main__":
    app.run(debug=True)
