from flask import Flask

def create_app(config_env = "development"):
    app = Flask(__name__)

    # Register blueprints here
    from .main import main as main_blueprint
    
    app.register_blueprint(main_blueprint, url_prefix="/")
    

    return app