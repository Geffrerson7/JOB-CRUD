from flask import Flask
from routes.jobs import jobs
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]  = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(jobs)


