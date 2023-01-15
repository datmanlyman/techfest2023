from flask import Flask, render_template, redirect, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    # simply redirect to /quiz route
    return redirect('/quiz')


@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/<path:path>")
def render_service_worker(path):
    return send_from_directory('./direct_static', path)
