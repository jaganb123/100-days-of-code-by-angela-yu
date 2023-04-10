from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("index.html", blogs=blog)

@app.route("/<int:index>")
def blog(index):
    blog = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    for i in blog:
        if i['id'] == index:
            blog_post = i
            break
    print(blog_post)
    return render_template("post.html", blogs=blog_post)



if __name__ == "__main__":
    app.run(debug=True)
