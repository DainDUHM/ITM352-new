from flask import Flask, render_template, request, redirect, url_for, session
import csv
import os
import datetime
import hashlib
from collections import defaultdict
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Constants for file names
USER_FILE = "users.csv"
TRANSACTION_FILE = "transactions.csv"

# Utility functions for hashing passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)

        if not os.path.exists(USER_FILE):
            with open(USER_FILE, 'w') as file:
                file.write("username,password\n")

        with open(USER_FILE, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([username, hashed_password])
        return redirect(url_for('login'))
    return render_template('create_account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)

        try:
            with open(USER_FILE, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) < 2:
                        continue
                    if row[0] == username and row[1] == hashed_password:
                        session['username'] = username
                        return redirect(url_for('home'))
            error = "Invalid username or password. Please try again."
        except FileNotFoundError:
            error = "User database not found. Please create an account first."

    return render_template('login.html', error=error)

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if 'username' not in session:
        return redirect(url_for('login'))

    error = None
    if request.method == 'POST':
        date = request.form.get('date')
        amount = request.form.get('amount')
        category = request.form.get('transaction_type')
        description = request.form.get('description')

        if not validate_date(date):
            error = "Invalid date format. Please use YYYY-MM-DD."
            return render_template('add_transaction.html', error=error)

        try:
            amount = float(amount)
        except ValueError:
            error = "Invalid amount. Please enter a valid number."
            return render_template('add_transaction.html', error=error)

        if not os.path.exists(TRANSACTION_FILE):
            with open(TRANSACTION_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["username", "date", "amount", "category", "description"])

        try:
            with open(TRANSACTION_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([session['username'], date, amount, category, description])
        except Exception as e:
            error = "An error occurred while saving the transaction. Please try again."
            return render_template('add_transaction.html', error=error)

        return redirect(url_for('home'))

    return render_template('add_transaction.html', error=error)


@app.route('/generate_summary')
def generate_summary():
    if 'username' not in session:
        return redirect(url_for('login'))

    total_income = 0
    total_expenses = 0
    transactions_found = False
    categories = defaultdict(float)
    timeline = defaultdict(float)

    if not os.path.exists(TRANSACTION_FILE):
        return render_template('summary.html', total_income=0, total_expenses=0, savings=0, categories={}, chart_data=None, timeline_chart=None, message="No transactions found.")

    with open(TRANSACTION_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) < 5:
                continue
            if row[0] == session['username']:
                transactions_found = True
                try:
                    amount = float(row[2])
                    category = row[3]
                    date = row[1]
                    if category == "Income":
                        total_income += amount
                    else:
                        total_expenses += abs(amount)
                        categories[category] += abs(amount)
                        timeline[date] += abs(amount)  # Add amount to timeline
                except ValueError:
                    continue

    if not transactions_found:
        return render_template('summary.html', total_income=0, total_expenses=0, savings=0, categories={}, chart_data=None, timeline_chart=None, message="No transactions found for this user.")

    savings = total_income - total_expenses

    # Generate pie chart for categories
    chart_data = None
    if categories:
        labels = list(categories.keys())
        values = list(categories.values())
        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        plt.title('Expenses by Category')
        plt.tight_layout()  # Prevent label overlap
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        chart_data = base64.b64encode(buf.getvalue()).decode()
        buf.close()

    # Generate timeline chart
    timeline_chart = None
    if timeline:
        dates = sorted(timeline.keys())
        amounts = [timeline[date] for date in dates]
        plt.figure(figsize=(10, 5))
        plt.plot(dates, amounts, marker='o', linestyle='-', color='blue', label='Expenses')
        plt.title('Timeline of Purchases')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.xticks(rotation=45, ha='right')  # Rotate date labels
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()  # Prevent label cutoff
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        timeline_chart = base64.b64encode(buf.getvalue()).decode()
        buf.close()

    return render_template('summary.html', total_income=total_income, total_expenses=total_expenses, savings=savings, categories=categories, chart_data=chart_data, timeline_chart=timeline_chart, message=None)

if __name__ == "__main__":
    app.run(debug=True)




