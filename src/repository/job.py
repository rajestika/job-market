from apps.src.main import cursor, connection
from apps.src.repository import sql_query

def get_job_list():
    cursor.execute(sql_query.FETCH_ALL_JOB_QUERY)

    record = cursor.fetchall()
    return record

def get_job_by_job_name(job_name):
    cursor.execute(sql_query.FETCH_JOB_BY_JOB_NAME_QUERY, (job_name,))

    record = cursor.fetchone()
    return record

def add_job(data, current_user):
    cursor.execute(sql_query.INSERT_JOB_QUERY, (current_user, data["job_name"], data["desc"], data["gaji"]))
    
    connection.commit()
    return

def add_application(data, current_user):
    cursor.execute(sql_query.INSERT_APPLICATION_QUERY, (current_user, data["job_id"]))

    connection.commit()
    return

def get_job_name_by_job_id(job_id):
    cursor.execute(sql_query.FETCH_JOB_NAME_BY_JOB_ID_QUERY, (job_id,))

    record = cursor.fetchone()
    return record

def get_job_ids_by_profile_id(profile_id):
    cursor.execute(sql_query.FETCH_JOB_IDS_BY_PROFILE_ID_QUERY, (profile_id,))

    record = cursor.fetchall()
    return record

def get_number_of_new_applicants_by_hr_id(hr_id):
    cursor.execute(sql_query.FETCH_NUMBER_OF_NEW_APPLICANTS_BY_HR_ID_QUERY, (hr_id,))

    record = cursor.fetchone()
    return record

def update_is_notified_to_true_by_hr_id(hr_id):
    cursor.execute(sql_query.UPDATE_IS_NOTIFIED_TO_TRUE_BY_HR_ID_QUERY, (hr_id,))

    connection.commit()

def get_job_and_hr_name(job_id):
    cursor.execute(sql_query.FETCH_JOB_AND_HR_NAME_BY_JOB_ID, (job_id,))
    
    record = cursor.fetchone()
    return record

def get_applicants_by_job_id(job_id):
    cursor.execute(sql_query.FETCH_APPLICANTS_BY_JOB_ID_QUERY, (job_id,))
    
    record = cursor.fetchall()
    return record

def update_application_status(job_id, applicant_id, job_status):
    if(job_status == "review"):
        cursor.execute(sql_query.UPDATE_APPLICATION_STATUS_QUERY, (job_status, job_id, applicant_id))

        connection.commit()
        return
    
    if(job_status == "accept"):
        cursor.execute(sql_query.UPDATE_APPLICATION_STATUS_QUERY, (job_status, job_id, applicant_id))

        connection.commit()
        return

    cursor.execute(sql_query.UPDATE_APPLICATION_STATUS_QUERY, (job_status, job_id, applicant_id))

    connection.commit()
    return

def get_job_id_by_hr_id(hr_id):
    cursor.execute(sql_query.FETCH_JOB_BY_HR_ID, (hr_id,))
    
    record = cursor.fetchall()
    return record