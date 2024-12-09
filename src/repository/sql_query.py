FETCH_PROFILE_BY_USERNAME_QUERY = "SELECT p.id, p.name, p.username, p.password, p.is_hr from profile p where p.username = %s"

FETCH_JOB_BY_PROFILE_ID_QUERY = "SELECT j.name, j.description as desc, j.gaji from job j join profile_job pj on j.id = pj.job_id where pj.profile_id = %s"

INSERT_PROFILE_QUERY = "INSERT INTO profile (id, name, username, password, is_hr) VALUES (%s, %s, %s, %s, %s)"

FETCH_ALL_USER_ID_QUERY = "SELECT p.id from profile p"

FETCH_ALL_JOB_QUERY = "SELECT j.name as job_name, j.description as desc, j.gaji from job j"

FETCH_JOB_BY_JOB_NAME_QUERY = "SELECT j.name, j.description as desc, j.gaji from job j where j.name = %s"

INSERT_JOB_QUERY = "INSERT INTO job (hr_id, name, description, gaji) VALUES (%s, %s, %s, %s)"

INSERT_APPLICATION_QUERY = "INSERT INTO profile_job (profile_id, job_id) VALUES (%s, %s)"

FETCH_JOB_NAME_BY_JOB_ID_QUERY = "SELECT j.name from job j where j.id = %s"

FETCH_JOB_ID_QUERY = "SELECT j.id from job j"

FETCH_PROFILE_NAME_BY_PROFILE_ID_QUERY = "SELECT p.name from profile p where p.id = %s"

FETCH_JOB_IDS_BY_PROFILE_ID_QUERY = "SELECT pj.job_id from profile_job pj where pj.profile_id = %s"

FETCH_NUMBER_OF_NEW_APPLICANTS_BY_HR_ID_QUERY = "SELECT COUNT(*) from profile_job pj join job j on pj.job_id = j.id where j.hr_id = %s and pj.is_notified = false"

UPDATE_IS_NOTIFIED_TO_TRUE_BY_HR_ID_QUERY = "UPDATE profile_job set is_notified = true from job j where profile_job.job_id = j.id and j.hr_id = %s"

FETCH_JOB_AND_HR_NAME_BY_JOB_ID = "SELECT j.name, j.description, j.gaji, p.name as hr  from job j join profile p on j.hr_id = p.id where j.id = %s"

FETCH_APPLICANTS_BY_JOB_ID = "SELECT p.name, p.id from profile p join profile_job pj on p.id = pj.profile_id where pj.job_id = %s"

UPDATE_STATUS_QUERY = "UPDATE profile_job set status = %s where job_id = %s and profile_id = %s"

FETCH_PROFILE_BY_UUID = "SELECT p.id, p.name, p.username, p.is_hr from profile p where p.id = %s"