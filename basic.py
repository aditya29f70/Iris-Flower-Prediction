from flask import Flask

app = Flask(__name__)  # Create the Flask app

@app.route('/')       # Route for /f
def home():
    return "<h1>hello</h1>"  # Return a simple HTML string

if __name__ == '__main__':   # Run this only if the script is executed directly
    app.run(debug=True)      # Start the Flask development server
