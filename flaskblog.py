from flask import Flask, render_template
app = Flask(__name__)


# version 0.1

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')
