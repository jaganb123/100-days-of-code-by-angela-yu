import random
from markupsafe import escape
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)

def validate(num):
    num = int(num)
    if num == random_number:
        return f'<h1 style="color:green">You found me!!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif num < random_number:
        return f'<h1 style="color:red">{num} is too low</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif num > random_number:
        return f'<h1 style="color:blue">{num} is too high</h1>' \
                '<img scr="https://media.giphy.com/media/3ohs7XRrW0HAoNqzUA/giphy.gif">'
    else:
        return '<p>Something went wrong</p>'

@app.route("/")
def home_page():
    return '<h1 style="text-align: left">Guess a number between 0 and 9</h1>' \
            '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

@app.route("/<num>")
def user_guess(num):
    html = validate(escape(num))
    return html


if __name__ == "__main__":
    app.run(debug=True)