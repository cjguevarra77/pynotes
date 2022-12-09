from flask import Flask

def create_app(config_env = "development"):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>PyNotes Home</h1>"

    @app.route("/about")
    def about():
        return "<h1>About PyNotes</h1>"

    return app