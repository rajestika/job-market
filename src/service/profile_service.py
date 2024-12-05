from apps.src.repository import profile, job
from apps.src.util import util
from apps.src.exception import exception

def login(data):
    username = data.get("username", None)
    password = data.get("password", None)
    
    if(util.check_none_in_array([username, password])):
        raise exception.InputDataNull

    username_result = profile.get_data_based_on_username(username)

    if(username_result is None):
        raise exception.UsernameNotFound
    
    if(password != username_result['password']):
        raise exception.PasswordIncorrect
    
    if(username_result["is_hr"]):
        number_of_new_applicants = job.get_number_of_new_applicants_by_hr_id(username_result["id"])
        
        job.update_is_notified_to_true_by_hr_id(username_result["id"])
        
        return f"{number_of_new_applicants['count']} new applicants"
    
    job_result = profile.get_job(username_result["id"])
    
    return {
            "name":username_result["name"],
            "username":username_result["username"],
            "password":username_result["password"],
            "job_applied":job_result
        }

def register(data):
    name = data.get("name", None)
    username = data.get("username", None)
    password = data.get("password", None)
    is_hr = data.get("is_hr", None)
    
    if(util.check_none_in_array([name, username, password, is_hr])):
        raise exception.InputDataNull
    
    username_result = profile.get_data_based_on_username(username)

    if(username_result):
        raise exception.DataAlreadyExist

    profile.add_new_data(data)

    return "register success"