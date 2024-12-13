class DataAlreadyExist(Exception):
    def __init__(self, message='data entry already esxist'):
        self.message = message
        super().__init__(message)

class InputDataNull(Exception):
    def __init__(self, message='bad input data'):
        self.message = message
        super().__init__(message)

class PasswordIncorrect(Exception):
    def __init__(self, message='password incorrect'):
        self.message = message
        super().__init__(message)

class DataNotFound(Exception):
    def __init__(self, message='data not found'):
        self.message = message
        super().__init__(message)

class Unauthorized(Exception):
    def __init__(self, message='you are not authorized'):
        self.message = message
        super().__init__(message)