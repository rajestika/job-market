from flask import Flask
import psycopg2
import psycopg2.extras

app = Flask(__name__)

connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

from apps.src.controller.profile_controller import profile_blueprint
from apps.src.controller.job_controller import job_blueprint

for blueprint in [profile_blueprint, job_blueprint]:
    app.register_blueprint(blueprint)