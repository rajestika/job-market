from flask import request, Blueprint
from apps.src.service import profile_service

profile_blueprint = Blueprint("profile_blueprint", __name__)

@profile_blueprint.post("/login")
def login():
    data = request.get_json()
    
    response = profile_service.login(data)
    return response

@profile_blueprint.post("/register")
def register():
    data = request.get_json()

    response = profile_service.register(data)
    return response