from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Set up the single route for '/'
@app.route('/')
def home():
    return "Welcome to a very boring web site!"

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
