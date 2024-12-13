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
@token_required
def show_detail_job_id(current_user, job_id):
    if (job_id is None):
        raise exception.InputDataNull
    
    response = make_response({
        "message":"request success",
        "data":job_service.job_details(current_user, job_id)
        }, 200)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicants")
@token_required
def applicants(current_user, job_id):
    if (job_id is None):
        raise exception.InputDataNull
    
    response = make_response({
        "message":"request success",
        "data":job_service.applicants(current_user, job_id)
        }, 200)
    return response

@job_blueprint.get("/jobs/<int:job_id>/applicants/<string:applicant_id>/<JobStatus:job_status>")
@token_required
def review(current_user, job_id, applicant_id, job_status):
    if(check_none_in_array([job_id, applicant_id, job_status])):
        raise exception.InputDataNull

    response = make_response({
        "message":job_service.review_application(current_user, job_id, applicant_id, job_status)
        }, 200)
    return response