from flask import request, Blueprint, make_response
from apps.src.repository import job
from apps.src.service import job_service
from apps.src.enum.enum import JobStatus
from apps.src.util.util import check_none_in_array

job_blueprint = Blueprint("job_blueprint", __name__)

@job_blueprint.get("/jobs")
def jobs():
    response = make_response({
        "message":"request success",
        "data":job_service.job_list()
        }, 200)
    return response

@job_blueprint.post("/jobs/add")
def add_job():
    data = request.get_json()

    response = make_response({
        "message":"job successfully added",
        "data":job_service.add_job(data)
        }, 201)
    return response

@job_blueprint.post("/apply")
def apply_job():
    data = request.get_json()

    response = make_response({
        "message":job_service.application(data)
        }, 201)
    return response

@job_blueprint.get("/jobs/<int:job_id>")
def show_detail_job_id(job_id):
    if (job_id is None):
        return{
            "message":"job_id should not be null"
        }
    
    response = make_response({
        "message":"request success",
        "data":job_service.job_details(job_id)
        }, 200)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicant/<int:applicant_id>/<JobStatus:job_status>")
def review(job_id, applicant_id, job_status):
    if(check_none_in_array([job_id, applicant_id, job_status])):
        return{
            "message":"job_id, applicant_id, or job_status should not be null"
        }

    response = make_response({
        "message":job_service.review_application(job_id, applicant_id, job_status)
        }, 200)
    return response