from flask import Flask, render_template, request, redirect, url_for
import os

# Create a Flask application instance
app = Flask(__name__)

# Ensure the 'templates' directory exists
if not os.path.exists('templates'):
    os.makedirs('templates')

# Create index.html file (quiz start page)
with open('templates/index.html', 'w') as f:
    f.write('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quiz Game</title>
    </head>
    <body>
        <h1>Welcome to the Quiz Game!</h1>
        <a href="{{ url_for('quiz') }}">Start the Quiz</a>
    </body>
    </html>
    ''')

# Create quiz.html file (quiz question page)
with open('templates/quiz.html', 'w') as f:
    f.write('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quiz Question</title>
    </head>
    <body>
        <h1>Question 1</h1>
        <form method="post" action="{{ url_for('quiz') }}">
            <p>What is the capital of France?</p>
            <input type="radio" name="answer" value="Paris" required> Paris<br>
            <input type="radio" name="answer" value="London"> London<br>
            <input type="radio" name="answer" value="Berlin"> Berlin<br><br>
            <button type="submit">Submit Answer</button>
        </form>
    </body>
    </html>
    ''')

# Create success.html file (quiz success page)
with open('templates/success.html', 'w') as f:
    f.write('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Success</title>
    </head>
    <body>
        <h1>Congratulations! You answered correctly!</h1>
        <a href="{{ url_for('home') }}">Go back to Home</a>
    </body>
    </html>
    ''')

# Set up the single route for '/'
@app.route('/')
def home():
    return render_template('index.html')

# Set up the route for '/quiz'
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'Paris':
            return redirect(url_for('success'))
        else:
            return "Incorrect answer. Please try again."
    return render_template('quiz.html')

# Set up the route for '/success'
@app.route('/success')
def success():
    return render_template('success.html')

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
