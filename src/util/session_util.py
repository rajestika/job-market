from flask import Flask, request, jsonify
from functools import wraps
import jwt
from apps.src.main import app
from apps.src.repository import profile

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        raw_token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            raw_token = request.headers['Authorization']
        
        token = raw_token.split('Bearer ')[1]
        
        # return 401 if raw_token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user_data = profile.get_profile_by_id(data["id"])
            current_user = current_user_data["id"]
            
        except Exception as e:
            return jsonify({
                'message' : str(e)
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated