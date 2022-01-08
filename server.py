from flask import Flask, app, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("sindex.html", num=rand_num, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template(
        "guess.html",
        user_name=name,
        gender_guess=gender,
        age_guess=age,
    )


@app.route("/blog")
def get_blog():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
