from flask import Flask
from routes.jobs import jobs

app = Flask(__name__)

app.register_blueprint(jobs)


