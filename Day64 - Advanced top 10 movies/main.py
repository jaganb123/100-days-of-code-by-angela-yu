from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, IntegerField
from wtforms.validators import DataRequired
import requests, os


with open(".env", "r") as file:
    for env in file.readlines():
        tmp = env.split()[0].split("=")
        os.environ[tmp[0]] = tmp[1]

THEMOVIEDB_API_KEY = os.environ['THEMOVIEDB_API_KEY']

def get_movies(query: str):
    header = {
        "Authorization": f"Bearer {THEMOVIEDB_API_KEY}"
    }
    params = {
        "query": query
    }
    url = "https://api.themoviedb.org/3/search/movie"
    response = requests.get(url, params=params, headers=header)
    movie_list = []
    for movie in response.json()['results']:
        movie_list.append({'id': movie['id'], 'title': movie['title'], 'release_date': movie['release_date']})
    global movies
    movies = movie_list    


global movies

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///best-movies.db" 
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        return(f'Title: {self.title}')
    
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    movie = StringField("Your Favorite Movie Here")
    submit = SubmitField("Done")

def get_movie_details(id: int):
    header = {
        "Authorization": f"Bearer {THEMOVIEDB_API_KEY}"
    }
    url = f"https://api.themoviedb.org/3/movie/{id}"
    response = requests.get(url, headers=header)
    movie_json = response.json()
    movie = Movie(
                title=movie_json.get('title'),
                year=movie_json.get('release_date'),
                description=movie_json.get('overview'),
                img_url=f"https://image.tmdb.org/t/p/w500{movie_json.get('poster_path')}"
            )
    return movie

def rank_movies():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    i = 1
    for movie in movies:
        movie.ranking = i
        i += 1
        # db.session.execute(db.update(movie))
    db.session.commit()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
with app.app_context():
    db.create_all()

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()



@app.route("/")
def home():
    movieList = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    return render_template("index.html", movie_list=movieList)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar_one()
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        rank_movies()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete", methods=["GET"])
def del_movie():
    movie_id = request.args.get("id")
    movie = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar_one()
    db.session.delete(movie)
    db.session.commit()
    rank_movies()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovie()
    print(request.method == "POST")
    if request.method == "POST":
        get_movies(str(form.movie.data))
        return redirect(url_for('select_movie'))
    else:
        return render_template("add.html", form=form)

@app.route("/select", methods=["GET", "POST"])
def select_movie():
    print(1, movies)
    return render_template("select.html", movie_list=movies)

@app.route("/adding_movie")
def add_to_db():
    movie_id = request.args.get('id')
    movie = get_movie_details(movie_id)
    db.session.add(movie)
    db.session.commit()
    movie = db.session.execute(db.select(Movie).filter_by(title=movie.title)).scalar_one()
    return redirect(url_for('rate_movie', id=movie.id))

if __name__ == '__main__':
    app.run(debug=True)
