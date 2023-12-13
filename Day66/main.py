from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")




# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    if request.method == "GET":
        result = db.session.execute(db.select(Cafe))
        all_cafe = result.scalars().all()
        random_cafe = random.choice(all_cafe)
        print(random_cafe)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def all_cafe():
    if request.method == "GET":
        result = db.session.execute(db.select(Cafe))
        all_cafe = result.scalars().all()
        dictionary = []
        for cafe in all_cafe:
            dictionary.append(cafe.to_dict())
    return jsonify(cafes=dictionary)

@app.route("/search", methods=["GET"])
def search_cafe():
    error_response = {"not found": None}
    if request.args.get("loc"):
        result = db.session.execute(db.select(Cafe).where(Cafe.location == request.args.get("loc"))).scalars().all()
        if result == []:
            error_response["not found"] = "Sorry, we don't have any cafe at that location."
            return jsonify(error=error_response)
        dictionary = []
        for cafe in result:
            dictionary.append(cafe.to_dict())
        return jsonify(dictionary)
    error_response["not found"] = "please use the query parameter loc=<location>"
    return jsonify(error=error_response)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    print(request.form)
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("loc"),
        seats = request.form.get("seat"),
        has_toilet = request.form.get("toilet"),
        has_wifi = request.form.get("wifi"),
        has_sockets = request.form.get("sockets"),
        can_take_calls = request.form.get("calls"),
        coffee_price = request.form.get("coffee_price") )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/test", methods=["POST"])
def test():
    print(request.form.keys())
    return jsonify(response={"Success": "POST request was success"})


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
