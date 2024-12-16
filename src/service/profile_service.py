from apps.src.repository import profile, job
from apps.src.util import util
from apps.src.exception import exception
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
from datetime import datetime, timedelta
from apps.src.main import app

def login(data):
    username = data.get("username", None)
    password = data.get("password", None)
    
    if(util.check_none_in_array([username, password])):
        raise exception.InputDataNull

    username_result = profile.get_profile_by_username(username)

    if(username_result is None):
        raise exception.DataNotFound("username not found")
    
    if(not check_password_hash(username_result["password"], password)):
        raise exception.PasswordIncorrect
    
    access_token = jwt.encode({
        'id':username_result["id"],
        "exp": datetime.utcnow() + timedelta(minutes = 30)
    }, app.config["SECRET_KEY"])

    refresh_token = jwt.encode({
        'id':username_result["id"],
        "exp": datetime.utcnow() + timedelta(days = 30)
    }, app.config["SECRET_KEY"])

    if(username_result["is_hr"]):
        number_of_new_applicants = job.get_number_of_new_applicants_by_hr_id(username_result["id"])
        
        job.update_is_notified_to_true_by_hr_id(username_result["id"])
        
        return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "name":username_result["name"],
            "notification":f"{number_of_new_applicants['count']} new applicants"
        }
    
    job_result = profile.get_job_by_profile_id(username_result["id"])
    
    return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "name":username_result["name"],
            "job_applied":job_result
        }

def register(data):
    name = data.get("name", None)
    username = data.get("username", None)
    password = data.get("password", None)
    is_hr = data.get("is_hr", None)
    
    if(util.check_none_in_array([name, username, password, is_hr])):
        raise exception.InputDataNull
    
    username_result = profile.get_profile_by_username(username)

    if(username_result):
        raise exception.DataAlreadyExist("username already exist")

    id = str(uuid.uuid1())
    data["password"] = generate_password_hash(data["password"])

    profile.add_new_profile(data, id)
    
    username_result = profile.get_profile_by_username(username)

    access_token = jwt.encode({
        'id':username_result["id"],
        "exp": datetime.utcnow() + timedelta(minutes = 30)
    }, app.config["SECRET_KEY"])

    refresh_token = jwt.encode({
        'id':username_result["id"],
        "exp": datetime.utcnow() + timedelta(days = 30)
    }, app.config["SECRET_KEY"])

    if(username_result["is_hr"]):
        number_of_new_applicants = job.get_number_of_new_applicants_by_hr_id(username_result["id"])
        
        job.update_is_notified_to_true_by_hr_id(username_result["id"])
        
        return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "name":username_result["name"],
            "notification":f"{number_of_new_applicants['count']} new applicants"
        }
    
    job_result = profile.get_job_by_profile_id(username_result["id"])
    
    return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "name":username_result["name"],
            "job_applied":job_result
        }

def refresh_token(current_user):
    access_token = jwt.encode({
        'id':current_user,
        "exp": datetime.utcnow() + timedelta(minutes = 30)
    }, app.config["SECRET_KEY"])
    
    return access_token