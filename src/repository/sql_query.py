FETCH_PROFILE_BY_USERNAME = "SELECT p.id, p.name, p.username, p.password from profile p where p.username = %s"

FETCH_JOB_BY_PROFILE_ID = "SELECT j.name, j.description as desc, j.gaji from job j join profile_job pj on j.id = pj.job_id where pj.profile_id = %s"

INSERT_PROFILE = "INSERT INTO profile (name, username, password) VALUES (%s, %s, %s)"

FETCH_ALL_USER_ID = "SELECT p.id from profile p"

FETCH_ALL_JOB = "SELECT j.name as job_name, j.description as desc, j.gaji from job j"

FETCH_JOB_BY_JOB_NAME = "SELECT j.name, j.description as desc, j.gaji from job j where j.name = %s"

INSERT_JOB = "INSERT INTO job (name, description, gaji) VALUES (%s, %s, %s)"

INSERT_APPLICATION = "INSERT INTO profile_job (profile_id, job_id) VALUES (%s, %s)"

FETCH_JOB_NAME_BY_JOB_ID = "SELECT j.name from job j where j.id = %s"

FETCH_JOB_ID = "SELECT j.id from job j"