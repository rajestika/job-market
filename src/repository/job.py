from apps.src.main import cursor, connection
from apps.src.repository import sql_query

def get_job_list():
    cursor.execute(sql_query.FETCH_ALL_JOB_QUERY)

    record = cursor.fetchall()
    return record

def get_job(job_name):
    cursor.execute(sql_query.FETCH_JOB_BY_JOB_NAME_QUERY, (job_name,))

    record = cursor.fetchone()
    return record

def add_job(data):
    cursor.execute(sql_query.INSERT_JOB_QUERY, (data["job_name"], data["desc"], data["gaji"]))
    
    connection.commit()
    return

def add_application(data):
    cursor.execute(sql_query.INSERT_APPLICATION_QUERY, (data["user_id"], data["job_id"]))

    connection.commit()
    return

def get_job_name(job_id):
    cursor.execute(sql_query.FETCH_JOB_NAME_BY_JOB_ID_QUERY, (job_id,))

    record = cursor.fetchone()
    return record

def get_job_id():
    cursor.execute(sql_query.FETCH_JOB_ID_QUERY)

    record = cursor.fetchall()
    return record

def get_job_ids_by_profile_id(profile_id):
    cursor.execute(sql_query.FETCH_JOB_IDS_BY_PROFILE_ID_QUERY, (profile_id,))

    record = cursor.fetchall()
    return record

def get_number_of_new_applicants_by_hr_id(hr_id):
    cursor.execute(sql_query.FETCH_NUMBER_OF_NEW_APPLICANTS_BY_HR_ID_QUERY, (hr_id,))

    record = cursor.fetchone()

    cursor.execute(sql_query.UPDATE_IS_NOTIFIED_TO_TRUE_BY_HR_ID_QUERY, (hr_id,))

    connection.commit()
    return record