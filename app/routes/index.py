from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.job import Job
from app.db import db

jobs_router = Blueprint("jobs", __name__)


@jobs_router.route("/")
def index():
    jobs = Job.query.all()
    return render_template("index.html", jobs=jobs)


@jobs_router.route("/new-job", methods=["GET", "POST"])
def create_job():
    if request.method == "GET":
        return render_template("create.html")
    
    elif request.method == "POST":
        name = request.form["name"]
        url = request.form["url"]
        company = request.form["company"]
        web_portal = request.form["web_portal"]
        modality = request.form["modality"]
        publicationDate = request.form["publicationDate"]

        new_job = Job(name, url, company, web_portal, modality, publicationDate)

        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for("jobs.index")), 201


@jobs_router.route("/update-job/<id>", methods=["GET", "PUT"])
def update_job(id):
    job = Job.query.get(id)

    if request.method == "GET":
        return render_template("update.html", job=job)

    elif request.method == "PUT":
        job.name = request.form["name"]
        job.url = request.form["url"]
        job.company = request.form["company"]
        job.web_portal = request.form["web_portal"]
        job.modality = request.form["modality"]
        job.publicationDate = request.form["publicationDate"]

        db.session.commit()

        return jsonify({"message": "Job updated successfully"}), 200


@jobs_router.route("/delete-job/<id>", methods=["DELETE"])
def delete_job(id):
    job = Job.query.get(id)
    db.session.delete(job)
    db.session.commit()

    return jsonify({"message": "Job deleted successfully"}), 204
