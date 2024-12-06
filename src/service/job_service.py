from apps.src.repository import job, profile
from apps.src.util import util
from apps.src.exception import exception

def job_list():
    job_list_result = job.get_job_list()
    return job_list_result
    

def add_job(data):
    name = data.get("job_name", None)
    desc = data.get("desc", None)
    gaji = data.get("gaji", None)

    if(util.check_none_in_array([name, desc, gaji])):
        raise exception.InputDataNull

    job_result = job.get_job(name)

    if(job_result):
        raise exception.DataAlreadyExist("job already exist")
    
    job.add_job(data)
    return "Job succesfully added"

def application(data):
    profile_id = data.get("user_id", None)
    job_id = data.get("job_id", None)

    if(util.check_none_in_array([profile_id, job_id])):
        raise exception.InputDataNull
    
    if(util.check_none_in_array([profile.get_user_by_user_id(profile_id), profile.get_job_by_job_id(job_id)])):
        raise exception.DataNotFound("profile id or job id not found")
    
    job_ids = job.get_job_ids_by_profile_id(profile_id)

    for id in job_ids:
        if job_id == id["job_id"]:
           raise exception.DataAlreadyExist("job already applied")
    
    job.add_application(data)
    return "Application success"

def job_details(job_id):
    job_record = job.get_job_and_hr_name(job_id)

    if(job_record is None):
        raise exception.DataNotFound("job not found")
    
    applicants_record = job.get_applicants_by_job_id(job_id)

    return {
            "job_information":job_record,
            "applicants":[applicant["name"] for applicant in applicants_record]
        }

def review_application(job_id, applicant_id, job_status):
    job_record = job.get_job_and_hr_name(job_id)

    if(job_record is None):
        raise exception.DataNotFound("job not found")

    applicants_record = job.get_applicants_by_job_id(job_id)

    ids = [applicant["id"] for applicant in applicants_record]

    if(applicant_id not in ids):
        raise exception.DataNotFound("applicant not found")

    status = job_status.value

    applicant_name = next((applicant["name"] for applicant in applicants_record if applicant["id"] == applicant_id), None)
    
    job.update_application_status(job_id, applicant_id, status)

    if(status == "review"):
        return f"Start reviewing {applicant_name}'s application for {job_record['name']} position"
    
    if(status == "accept"):
        return f"{applicant_name}'s application has been accepted for {job_record['name']} position"
    
    return f"{applicant_name}'s application has been rejected for {job_record['name']} position"
