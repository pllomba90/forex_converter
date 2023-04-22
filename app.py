### Base  application code
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = 'dolladollabills'
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("index.html")