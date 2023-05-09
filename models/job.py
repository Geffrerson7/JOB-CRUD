from database.db import db
from sqlalchemy.sql import func

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    url = db.Column(db.String(500))
    company = db.Column(db.String(200))
    web_portal= db.Column(db.String(100))
    modality = db.Column(db.String(100))
    applicationDate = db.Column(db.Date(), default=func.now())
    publicationDate = db.Column(db.Date)

    def __init__(self, name, url, company, web_portal, modality, applicationDate, publicationDate):
        self.name = name
        self.url = url
        self.company = company
        self.web_portal = web_portal
        self.modality = modality
        self.applicationDate = applicationDate
        self.publicationDate = publicationDate
