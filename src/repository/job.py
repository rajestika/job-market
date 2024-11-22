from apps.src.main import cursor, connection
import sql_query

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