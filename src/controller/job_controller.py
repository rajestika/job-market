from flask import request, Blueprint
from apps.src.repository import job
from apps.src.service import job_service

job_blueprint = Blueprint("job_blueprint", __name__)

@job_blueprint.get("/jobs")
def jobs():
    response = job.get_job_list()
    return response

@job_blueprint.post("/jobs/add")
def add_job():
    data = request.get_json()

    response = job_service.add_job(data)
    return response

@job_blueprint.post("/apply")
def apply_job():
    data = request.get_json()

    response = job_service.application(data)
    return response

@job_blueprint.get("/jobs/<int:job_id>")
def show_detail_job_id(job_id):
    response = job_service.job_details(job_id)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicant/<int:applicant_id>/review")
def review(job_id, applicant_id):
    response = job_service.review_application(job_id, applicant_id)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicant/<int:applicant_id>/accept")
def accept(job_id, applicant_id):
    response = job_service.accept_application(job_id, applicant_id)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicant/<int:applicant_id>/reject")
def reject(job_id, applicant_id):
    response = job_service.reject_application(job_id, applicant_id)
    return response