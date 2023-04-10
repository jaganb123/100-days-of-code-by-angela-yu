from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_user():
    return "Hello"

@app.route('/<username>/home')
def home_message(username):
    return f"Welcome to my home {username}"

if __name__ == "__main__":
    app.run(debug=True)
