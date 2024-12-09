from flask import request, Blueprint, make_response
from apps.src.service import profile_service
from apps.src.util.session_util import token_required
from apps.src.repository import profile

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

@profile_blueprint.get("/profile")
@token_required
def get_profile(current_user):
    response = make_response({
        "message":"request success",
        "data":profile.get_profile_by_id(current_user)
    })
    return response