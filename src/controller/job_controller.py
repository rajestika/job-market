from flask import request, Blueprint, make_response
from apps.src.service import job_service
from apps.src.util.util import check_none_in_array
from apps.src.exception import exception

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
        "message":job_service.add_job(data)
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
        raise exception.InputDataNull
    
    response = make_response({
        "message":"request success",
        "data":job_service.job_details(job_id)
        }, 200)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicant/<int:applicant_id>/<JobStatus:job_status>")
def review(job_id, applicant_id, job_status):
    if(check_none_in_array([job_id, applicant_id, job_status])):
        raise exception.InputDataNull

    response = make_response({
        "message":job_service.review_application(job_id, applicant_id, job_status)
        }, 200)
    return response