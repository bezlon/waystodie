from random_way_to_die import random_way_to_die
from flask import render_template, url_for, redirect, Flask, flash

app = Flask(__name__)


@app.route("/home")
def home():
	return render_template("index.html", wtd=str(random_way_to_die()))

@app.route("/")
def redirect_():
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug=True)