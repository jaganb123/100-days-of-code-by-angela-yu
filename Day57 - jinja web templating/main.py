from flask import Flask, render_template
import datetime, requests

app = Flask(__name__)

def gender_predict(name):
    gender_url = f'https://api.genderize.io?name={name}'
    response = requests.get(url=url)
    return response.json()['gender']

@app.route('/')
def home():
    year = datetime.date.today().year
    return render_template('index.html', year=year)

@app.route('/guess/<name>')
def guess_user(name):
    user_name = str(name).capitalize()
    age_url = f'https://api.agify.io?name={name}'
    gender_url = f'https://api.genderize.io?name={name}'
    user_age = requests.get(url=age_url).json()['age']
    user_gender = requests.get(url=gender_url).json()['gender']
    context = {
        'name': user_name,
        'age': user_age,
        'gender': user_gender
    }          
    return render_template('user_prediction.html', **context)

@app.route('/')
def blog():
    blog = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    print(blog)
    return render_template('blog.html', blogs=blog)

if __name__ == "__main__":
    app.run(debug=True)