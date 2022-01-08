from flask import Flask, app, render_template
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=rand_num, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
