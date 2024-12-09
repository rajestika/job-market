from flask import request, Blueprint, make_response
from apps.src.service import job_service
from apps.src.util.util import check_none_in_array
from apps.src.exception import exception
from apps.src.util.session_util import token_required

job_blueprint = Blueprint("job_blueprint", __name__)

@job_blueprint.get("/jobs")
def jobs():
    response = make_response({
        "message":"request success",
        "data":job_service.job_list()
        }, 200)
    return response

@job_blueprint.post("/jobs/add")
@token_required
def add_job(current_user):
    data = request.get_json()

    response = make_response({
        "message":job_service.add_job(data, current_user)
        }, 201)
    return response

@job_blueprint.post("/jobs/apply")
@token_required
def apply_job(current_user):
    data = request.get_json()

    response = make_response({
        "message":job_service.application(data, current_user)
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
@token_required
def review(job_id, applicant_id, job_status):
    if(check_none_in_array([job_id, applicant_id, job_status])):
        raise exception.InputDataNull

    response = make_response({
        "message":job_service.review_application(job_id, applicant_id, job_status)
        }, 200)
    return response