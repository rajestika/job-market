from apps.src.repository import job, profile
from apps.src.util import util
from apps.src.exception import exception
from apps.src.enum.enum import JobStatus

def job_list():
    job_list_result = job.get_job_list()
    return job_list_result

def add_job(data, current_user):
    is_hr = profile.get_profile_by_id(current_user)["is_hr"]
    if (not is_hr):
        raise exception.Unauthorized
    
    name = data.get("job_name", None)
    desc = data.get("desc", None)
    gaji = data.get("gaji", None)

    if(util.check_none_in_array([name, desc, gaji])):
        raise exception.InputDataNull

    job_result = job.get_job_by_job_name(name)

    if(job_result):
        raise exception.DataAlreadyExist("job already exist")
    
    job.add_job(data, current_user)
    return "job succesfully added"

def application(data, current_user):
    is_hr = profile.get_profile_by_id(current_user)["is_hr"]
    if (is_hr):
        raise exception.Unauthorized
    
    job_id = data.get("job_id", None)

    if(not job_id):
        raise exception.InputDataNull
    
    if(not job.get_job_name_by_job_id(job_id)):
        raise exception.DataNotFound("job not found")
    
    job_ids = job.get_job_ids_by_profile_id(current_user)

    for id in job_ids:
        if job_id == id["job_id"]:
           raise exception.DataAlreadyExist("job already applied")
    
    job.add_application(data, current_user)
    return "application success"

def job_details(current_user, job_id):
    is_hr = profile.get_profile_by_id(current_user)["is_hr"]
    if (not is_hr):
        raise exception.Unauthorized
    
    job_record = job.get_job_and_hr_name(job_id)
    if(job_record is None):
        raise exception.DataNotFound("job not found")
    
    hr_job = job.get_job_id_by_hr_id(current_user)
    hr_job_id = [job["id"] for job in hr_job]
    if (job_id not in hr_job_id):
        raise exception.Unauthorized

    return {
            "job_information":job_record
    }

def applicants(current_user, job_id):
    is_hr = profile.get_profile_by_id(current_user)["is_hr"]
    if (not is_hr):
        raise exception.Unauthorized
    
    job_record = job.get_job_name_by_job_id(job_id)
    if(job_record is None):
        raise exception.DataNotFound("job not found")
    
    hr_job = job.get_job_id_by_hr_id(current_user)
    hr_job_id = [job["id"] for job in hr_job]
    if (job_id not in hr_job_id):
        raise exception.Unauthorized
    
    applicants_record = job.get_applicants_by_job_id(job_id)
    
    return {
            "applicants":applicants_record
    }

def review_application(current_user, job_id, applicant_id, job_status):
    is_hr = profile.get_profile_by_id(current_user)["is_hr"]
    if (not is_hr):
        raise exception.Unauthorized
    
    job_record = job.get_job_and_hr_name(job_id)
    if(job_record is None):
        raise exception.DataNotFound("job not found")
    
    hr_job = job.get_job_id_by_hr_id(current_user)
    hr_job_id = [job["id"] for job in hr_job]
    if (job_id not in hr_job_id):
        raise exception.Unauthorized

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
