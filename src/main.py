from flask import Flask
import psycopg2
import psycopg2.extras
from apps.src.enum.enum import JobStatus, JobStatusConverter
from apps.src.exception import exception_register
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logFormatter = logging.basicConfig(filename='logs.log', format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey123"

app.url_map.converters["JobStatus"] = JobStatusConverter

exception_register.register_exception(app)

connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

from apps.src.controller.profile_controller import profile_blueprint
from apps.src.controller.job_controller import job_blueprint

for blueprint in [profile_blueprint, job_blueprint]:
    app.register_blueprint(blueprint)