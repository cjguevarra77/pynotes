from . import main

@main.route("/")
@main.route("/home")
@main.route("/index")
def index():
    return "<h1>PyNotes: Simple, easy-to-use note keeping web app </h1>"

@main.route('/about')
def about():
    return "<h1>About PyNotes</h1>"