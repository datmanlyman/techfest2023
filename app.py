from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    # simply redirect to /quiz route
    return redirect('/quiz')


@app.route("/quiz")
def quiz():
    return render_template('quiz.html')