from flask import Flask, app, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=rand_num, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    user_name = name.title()
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template(
        "guess.html",
        user_name=user_name,
        gender_guess=gender,
        age_guess=age,
    )


if __name__ == "__main__":
    app.run()
