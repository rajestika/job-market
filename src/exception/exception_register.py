from flask import jsonify
from apps.src.exception import exception

def register_exception(app):
    @app.errorhandler(exception.DataAlreadyExist)
    def handle_data_already_exist(e):
        response = jsonify({"message": str(e)})
        response.status_code = 200
        return response
    
    @app.errorhandler(exception.InputDataNull)
    def handle_input_data_null(e):
        response = jsonify({"message": str(e)})
        response.status_code = 400
        return response
    
    @app.errorhandler(exception.PasswordIncorrect)
    def handle_password_incorrect(e):
        response = jsonify({"message": str(e)})
        response.status_code = 400
        return response
    
    @app.errorhandler(exception.DataNotFound)
    def handle_data_not_found(e):
        response = jsonify({"message": str(e)})
        response.status_code = 404
        return response
    
    @app.errorhandler(LookupError)
    def handle_lookup_error(e):
        response = jsonify({"message": str(e)})
        response.status_code = 404
        return response