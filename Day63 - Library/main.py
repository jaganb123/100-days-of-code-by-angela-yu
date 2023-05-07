from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# db.create_all()
all_books = []

@app.route('/')
def home():
    return render_template('index.html', book_list=db.session().query(Book).all())


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=request.form["rating"]
                        )
        db.session.add(new_book)
        db.session.commit()
        
    return render_template('add.html')

@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    # print(id)
    book = Book.query.get(id)
    if request.method == 'POST':
        book.rating = request.form["rating"]
        db.session.commit()
    return render_template('edit.html', book=book)

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

# with app.app_context():
#     book = Book.query.get(1)
#     print(book.title)

# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('edit', id=1))

if __name__ == "__main__":
    app.run(debug=True)
