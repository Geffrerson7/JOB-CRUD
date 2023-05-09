from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .routes.index import jobs_router
from app.db import db


def create_app():
    
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
    app.register_blueprint(jobs_router)
    db.init_app(app)
    
    return app
