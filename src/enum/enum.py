from enum import Enum
from werkzeug.routing import BaseConverter

class JobStatusConverter(BaseConverter):
    """Custom URL Converter for JobStatus Enum"""
    def __init__(self, map):
        super().__init__(map)
        self.enum = JobStatus

    def to_python(self, value):
        # Convert the string from the URL into a JobStatus enum member
        try:
            return self.enum(value)
        except ValueError:
            raise LookupError(f"Invalid JobStatus: {value}")

    def to_url(self, value):
        # Convert a JobStatus enum member back into a string for the URL
        return value.value

class JobStatus(Enum):
    REVIEW = "review"
    ACCEPT = "accept"
    REJECT = "reject"