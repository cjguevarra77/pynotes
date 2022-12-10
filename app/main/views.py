from . import main
from flask import render_template

@main.route("/")
@main.route("/home")
@main.route("/index")
def index():
    
    return render_template("main/index.html", title="PyNotes Home", content="PyNotes: Simple, easy-to-use note keeping web app ")

@main.route('/about')
def about():
    return render_template("main/about.html", title="About PyNotes", content="PyNotes: Simple, easy-to-use note keeping web app ")