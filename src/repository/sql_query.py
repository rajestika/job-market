FETCH_PROFILE_BY_USERNAME_QUERY = "SELECT p.id, p.name, p.username, p.password from profile p where p.username = %s"

FETCH_JOB_BY_PROFILE_ID_QUERY = "SELECT j.name, j.description as desc, j.gaji from job j join profile_job pj on j.id = pj.job_id where pj.profile_id = %s"

INSERT_PROFILE_QUERY = "INSERT INTO profile (name, username, password, is_hr) VALUES (%s, %s, %s, %s)"

FETCH_ALL_USER_ID_QUERY = "SELECT p.id from profile p"

FETCH_ALL_JOB_QUERY = "SELECT j.name as job_name, j.description as desc, j.gaji from job j"

FETCH_JOB_BY_JOB_NAME_QUERY = "SELECT j.name, j.description as desc, j.gaji from job j where j.name = %s"

INSERT_JOB_QUERY = "INSERT INTO job (name, description, gaji) VALUES (%s, %s, %s)"

INSERT_APPLICATION_QUERY = "INSERT INTO profile_job (profile_id, job_id) VALUES (%s, %s)"

FETCH_JOB_NAME_BY_JOB_ID_QUERY = "SELECT j.name from job j where j.id = %s"

FETCH_JOB_ID_QUERY = "SELECT j.id from job j"

FETCH_PROFILE_NAME_BY_PROFILE_ID_QUERY = "SELECT p.name from profile p where p.id = %s"

FETCH_JOB_IDS_BY_PROFILE_ID_QUERY = "SELECT pj.job_id from profile_job pj where pj.profile_id = %s"