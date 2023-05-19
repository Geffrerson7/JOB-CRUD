from app import create_app, db
from flask_migrate import Migrate
from app.models.job import Job

app = create_app()
migrate = Migrate(app, db) 