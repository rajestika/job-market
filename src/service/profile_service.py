from apps.src.repository import profile, job
from apps.src.util import util

def login(data):
    username = data.get("username", None)
    password = data.get("password", None)
    
    if(util.check_none_in_array([username, password])):
        return {
            "message":"Please input username and password"
        }, 400

    username_result = profile.get_data_based_on_username(username)

    if(username_result is None):
        return{
            "message":"Username not found"
        }, 400
    
    if(password != username_result['password']):
        return {
                "message":"Password incorrect"
            }, 400
    
    if(username_result["is_hr"]):
        number_of_new_applicants = job.get_number_of_new_applicants_by_hr_id(username_result["id"])
        
        job.update_is_notified_to_true_by_hr_id(username_result["id"])
        
        return{
            "message":f"Login success, there are {number_of_new_applicants['count']} new applicant(s) applied for your job",
            }, 200
    
    job_result = profile.get_job(username_result["id"])
    
    return {
        "message":"Login Sunccess",
        "data":{
            "name":username_result["name"],
            "username":username_result["username"],
            "password":username_result["password"],
            "job_applied":job_result
        }
    }, 200

def register(data):
    name = data.get("name", None)
    username = data.get("username", None)
    password = data.get("password", None)
    is_hr = data.get("is_hr", None)
    
    if(util.check_none_in_array([name, username, password, is_hr])):
        return {
            "message":"Please input your data"
        }, 400
    
    username_result = profile.get_data_based_on_username(username)

    if(username_result):
        return {
            "message":"Username already registered"
        }, 400

    profile.add_new_data(data)

    return{
        "message":"Register success"
    }, 200