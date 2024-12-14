from apps.src.main import cursor, connection
from apps.src.repository import sql_query

def get_profile_by_username(username):
    cursor.execute(sql_query.FETCH_PROFILE_BY_USERNAME_QUERY, (username,))

    record = cursor.fetchone()
    return  record

def get_job_by_profile_id(profile_id):
    cursor.execute(sql_query.FETCH_JOB_BY_PROFILE_ID_QUERY, (profile_id,))

    record = cursor.fetchall()
    return record

def add_new_profile(data, id):
    cursor.execute(sql_query.INSERT_PROFILE_QUERY, (id, data["name"], data["username"], data["password"], data["is_hr"]))
    
    connection.commit()
    return

def get_profile_by_id(id):
    cursor.execute(sql_query.FETCH_PROFILE_BY_ID_QUERY, (id,))
    record = cursor.fetchone()

    return record