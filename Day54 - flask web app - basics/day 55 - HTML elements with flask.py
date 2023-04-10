from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        string = str(function())
        return f"<b>{string}</b>"
    return wrapper_function

def make_empasis(function):
    def wrapper_function():
        string = str(function())
        return f"<em>{string}</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        string = str(function())
        return f"<u>{string}</u>"
    return wrapper_function


@app.route('/')
@make_bold
@make_empasis
@make_underline
def hello_user():
    return "Hello"

@app.route('/<username>/home')
def home_message(username):
    return ('<h1 style= text-align:center >"Welcome to my home"</h1>'
            f'<p>"This home is made using the flask web server"</p>'
            '<img src=https://foyr.com/learn/wp-content/uploads/2021/08/design-your-dream-home.jpg width=400px>'
    )
            

if __name__ == "__main__":
    app.run(debug=True)
