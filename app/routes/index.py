from flask import Blueprint, render_template, request, redirect, url_for
from app.models.job import Job
from app.db import db

jobs_router = Blueprint('jobs', __name__)

@jobs_router.route("/")
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@jobs_router.route("/new-job", methods=['POST'])
def create_job():
    name = request.form["name"]
    url = request.form["url"]
    company = request.form["company"]
    web_portal = request.form["web_portal"]
    modality = request.form["modality"] 
    publicationDate = request.form["publicationDate"]

    new_job=Job(name, url, company, web_portal, modality, publicationDate)
    
    db.session.add(new_job)
    db.session.commit()

    return redirect(url_for('jobs.index'))

@jobs_router.route("/update-job")
def update_job():
    return "Updating a job"

@jobs_router.route("/delete-job/<id>")
def delete_job(id):
    job = Job.query.get(id)
    db.session.delete(job)
    db.session.commit()

    return redirect(url_for('jobs.index'))