from flask import request, Blueprint, make_response
from apps.src.service import profile_service

profile_blueprint = Blueprint("profile_blueprint", __name__)

@profile_blueprint.post("/login")
def login():
    data = request.get_json()
    
    response = make_response({
        "message":"login success",
        "data":profile_service.login(data)
        }, 200)
    return response

@profile_blueprint.post("/register")
def register():
    data = request.get_json()

    response = make_response({
        "message":profile_service.register(data)
        }, 201)
    return response