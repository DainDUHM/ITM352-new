from flask import Flask, render_template, request, redirect, url_for, session, make_response
import csv
import datetime
import os
import hashlib

app = Flask(__name__)
app.secret_key = 'supersecretkey'

database_file = 'finance_users.csv'
transactions_file = 'transactions.csv'

# Function to create a new account
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        with open(database_file, 'a', newline='') as db:
            writer = csv.writer(db)
            writer.writerow([username, hashed_password])
        return redirect(url_for('login'))
    return render_template('create_account.html')

# Function to authenticate login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        with open(database_file, 'r') as db:
            reader = csv.reader(db)
            for row in reader:
                if row[0] == username and row[1] == hashed_password:
                    session['username'] = username
                    return redirect(url_for('dashboard'))
        return "Invalid username or password."
    return render_template('login.html')

# Dashboard after login
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('dashboard.html', username=username)

# Function to add a transaction
@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    if request.method == 'POST':
        date = request.form['date']
        if not validate_date(date):
            return "Invalid date format."
        
        amount = request.form['amount']
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError:
            return "Invalid amount."
        
        category = request.form['category']
        description = request.form['description']
        
        with open(transactions_file, 'a', newline='') as tf:
            writer = csv.writer(tf)
            writer.writerow([username, date, amount, category, description])
        return redirect(url_for('dashboard'))
    return render_template('add_transaction.html')

# Function to validate date format
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to view transaction summary
@app.route('/view_summary')
def view_summary():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    total_income = 0
    total_expense = 0
    
    with open(transactions_file, 'r') as tf:
        reader = csv.reader(tf)
        for row in reader:
            if row[0] == username:
                amount = float(row[2])
                if amount > 0:
                    total_income += amount
                else:
                    total_expense += amount
    
    return render_template('view_summary.html', total_income=total_income, total_expense=-total_expense, total_savings=total_income + total_expense)

# Function to set a monthly budget
@app.route('/set_budget', methods=['GET', 'POST'])
def set_monthly_budget():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    if request.method == 'POST':
        budget = request.form['budget']
        try:
            budget = float(budget)
            if budget < 0:
                raise ValueError("Budget cannot be negative.")
        except ValueError:
            return "Invalid budget amount."
        
        with open(database_file, 'a', newline='') as db:
            writer = csv.writer(db)
            writer.writerow([username, 'budget', budget])
        return redirect(url_for('dashboard'))
    return render_template('set_budget.html')

# Route to logout user
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
