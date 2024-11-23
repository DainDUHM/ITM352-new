from flask import Flask, render_template, request, redirect, url_for, session, make_response
import json
import random
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load questions from JSON file
def load_questions():
    # Hardcode the full absolute path to your questions.json file
    file_path = r'C:\Users\User\Documents\GitHub\ITM352-new\A3\questions.json'
    # Attempt to open the file
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        return []
    with open(file_path, 'r') as file:
        return json.load(file)

# Load leaderboard from JSON file
def load_leaderboard():
    try:
        with open('leaderboard.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save leaderboard to JSON file
def save_leaderboard(leaderboard):
    with open('leaderboard.json', 'w') as file:
        json.dump(leaderboard, file)

# Route to handle login, set cookie, and redirect to home
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        # Set a cookie to remember the user
        response = make_response(redirect(url_for('home')))
        response.set_cookie('username', username)
        return response
    return render_template('login.html')

# Route to the home page, which shows the quiz or a welcome back page
@app.route('/')
def home():
    # Check if the user has visited before using cookies
    username = request.cookies.get('username')
    if username and 'restart' not in session:
        session['username'] = username
        # Load user's score history if it exists
        score_history = session.get('score_history', [])
        return render_template('welcome_back.html', username=username, score_history=score_history)

    # If user has not visited before, redirect to login
    if 'username' not in session:
        return redirect(url_for('login'))

    # Set up quiz for first-time users or users restarting the quiz
    questions = load_questions()
    random.shuffle(questions)  
    session['questions'] = questions
    session['current_question'] = 0
    session['score'] = 0
    # Remove 'restart' flag if it exists
    session.pop('restart', None)

    return render_template('index.html', question=randomize_options(questions[0]))

# Route to handle answer submissions and provide real-time feedback
@app.route('/answer', methods=['POST'])
def answer():
    user_answer = request.form['answer']
    question_index = session.get('current_question', 0)
    questions = session.get('questions', [])

    feedback = ""
    if question_index < len(questions):
        correct_answer = questions[question_index]['correct']
        if user_answer == correct_answer:
            feedback = "Correct!"
            session['score'] += 1
        else:
            feedback = f"Incorrect! The correct answer was: {correct_answer}"

        session['current_question'] = question_index + 1
        if session['current_question'] < len(questions):
            next_question = randomize_options(questions[session['current_question']])
            return render_template('index.html', question=next_question, feedback=feedback)
        else:
            return redirect(url_for('result'))

# Route to display the result and add to leaderboard
@app.route('/result')
def result():
    score = session.get('score', 0)
    username = session.get('username', 'Guest')

    # Save score in user's score history (stored in session)
    score_history = session.get('score_history', [])
    score_history.append(score)
    session['score_history'] = score_history

    # Load leaderboard, add current score, and save it
    leaderboard = load_leaderboard()
    leaderboard.append({'username': username, 'score': score})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]
    save_leaderboard(leaderboard)

    return render_template('result.html', score=score, leaderboard=leaderboard)

# Utility function to randomize the options of a question
def randomize_options(question):
    options = question['options']
    random.shuffle(options)
    question['options'] = options
    return question

# Route to clear session and restart the quiz
@app.route('/restart-quiz')
def restart_quiz():
    session['restart'] = True
    return redirect(url_for('home'))

# Route to clear session and logout user
@app.route('/clear-session')
def clear_session():
    session.clear()
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == "__main__":
    app.run(debug=True)



