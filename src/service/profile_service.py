from apps.src.repository import profile
from apps.src.util import util
import json

def login(data):
    username = data.get("username", None)
    password = data.get("password", None)
    
    if(util.check_none_in_array([username, password])):
        return {
            "message":"Please input username and password"
        }

    username_result = profile.get_data_based_on_username(username)

    if(username_result is None):
        return{
            "message":"Username not found"
        }
    
    if(password != username_result['password']):
        return {
                "message":"Password incorrect"
            }
    
    job_result = profile.get_job(username_result["id"])
    
    return json.dumps({
        "name":username_result["name"],
        "username":username_result["username"],
        "password":username_result["password"],
        "job_applied":job_result
    }, indent=4)

def register(data):
    name = data.get("name", None)
    username = data.get("username", None)
    password = data.get("password", None)
    is_hr = data.get("is_hr", None)
    
    if(util.check_none_in_array([name, username, password, is_hr])):
        return {
            "message":"Please input your data"
        }
    
    username_result = profile.get_data_based_on_username(username)

    if(username_result):
        return {
            "message":"Username already registered"
        }

    profile.add_new_data(data)

    return{
        "message":"Register success"
    }