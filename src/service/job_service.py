from apps.src.repository import job, profile
import json

def add_job(data):
    name = data.get("job_name", None)
    desc = data.get("desc", None)
    gaji = data.get("gaji", None)

    if(name==None or desc==None or gaji==None):
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

    if(profile_id==None or job_id==None):
        return {
            "message":"Please input your data"
        }

    dict_user_id = profile.get_user_id()
    dict_job_id = job.get_job_id()

    user_ids = [id["id"] for id in dict_user_id]
    job_ids = [id["id"] for id in dict_job_id]

    if(profile_id not in user_ids or job_id not in job_ids):
        return{
            "message":"User_id or job_id not registered yet"
        }

    job_user = profile.get_job(profile_id)

    if(len(job_user) == 0):
        job.add_application(data)
        return {
            "message":"Application success"
        }

    if(len(job_user) != 0):
        job_name = job.get_job_name(job_id)
        for application in job_user:
            if application["name"] == job_name["name"]:
                return{
                    "message":all_user_id
                }
        job.add_application(data)
        return {
            "message":"Application success"
        }
        
    
    