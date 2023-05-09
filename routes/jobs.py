from flask import Blueprint, render_template

jobs = Blueprint('jobs', __name__)

@jobs.route("/")
def home():
    return render_template('index.html')

@jobs.route("/new-job")
def create_job():
    return "Saving a job"

@jobs.route("/update-job")
def update_job():
    return "Updating a job"

@jobs.route("/delete-job")
def delete_job():
    return "Deleting a contact"