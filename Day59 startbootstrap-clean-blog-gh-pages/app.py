from flask import Flask, render_template, request
import requests, smtplib

app = Flask(__name__)

def send_email(to_mail, message):
    my_email = "birthday_wishes1@outlook.com"
    # password = "AXh9*)f+d1*GQO0"
    app_password = "ignjjolojotnbvjj"
    server = "outlook.office365.com"
    con = smtplib.SMTP(server, port=587)
    con.starttls()
    con.login(user=my_email, password=app_password)
    con.sendmail(from_addr=my_email, to_addrs=to_mail, msg=f"Subject:Contact Me Form\n\n{message}")

def get_blog():
    url="https://api.npoint.io/ba823ce5529e820110ca"
    response = requests.get(url)
    return response.json()

@app.route("/")
def home():
    blog=get_blog()
    # print(blog)
    return render_template("index.html", blog_post=blog)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        message = (f"name: {data['name']}\n"
                   f"email: {data['email']}\n"
                   f"phone: {data['phone']}\n"
                   f"message: {data['message']}")
        send_email("jagan2221997@gmail.com", message)
        return render_template("contact.html", message="Successfully sent the message")
    else:
        return render_template("contact.html", message="Contact Me")

@app.route("/post/<id>")
def post(id):
    blog=next((blog for  blog in get_blog() if str(blog["id"]) == id), None)
    return render_template("post.html", blog_post=blog)

if __name__ == "__main__":
    app.run(debug=True)
