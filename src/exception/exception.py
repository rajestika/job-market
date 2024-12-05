class DataAlreadyExist(Exception):
    def __init__(self, message='data entry already esxist'):
        self.message = message
        super().__init__(message)

class InputDataNull(Exception):
    def __init__(self, message='bad input data'):
        self.message = message
        super().__init__(message)

class UsernameNotFound(Exception):
    def __init__(self, message='username not found'):
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