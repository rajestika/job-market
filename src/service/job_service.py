from apps.src.repository import job, profile
from apps.src.util import util
import json

def add_job(data):
    name = data.get("job_name", None)
    desc = data.get("desc", None)
    gaji = data.get("gaji", None)

    if(util.check_none_in_array([name, desc, gaji])):
        return {
            "message":"Please input your data"
        }

    job_result = job.get_job(name)

    if(job_result):
        return {
            "message":"Job already exist"
        }
    
    job.add_job(data)
    return {
        "message":"Job succesfully added"
    }

def application(data):
    profile_id = data.get("user_id", None)
    job_id = data.get("job_id", None)

    if(util.check_none_in_array([profile_id, job_id])):
        return {
            "message":"Please input your data"
        }
    
    if(util.check_none_in_array(profile.get_user_by_user_id_and_get_job_by_job_id(profile_id, job_id))):
        return {
            "message":"User_id or job_id not registered yet"
        }

    job_ids = job.get_job_ids_by_profile_id(profile_id)

    if(job_id in job_ids["id"]):
        return {
            "message":"Job already applied"
        }
    
    job.add_application(data)
    return {
        "message":"Application success"
    }
