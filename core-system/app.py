from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL (homepage)
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1><p>Welcome to my Flask app.</p>"

# Run the app locally if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)

