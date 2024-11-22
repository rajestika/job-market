from apps.src.main import cursor, connection
import sql_query

def get_data_based_on_username(username):
    cursor.execute(sql_query.FETCH_PROFILE_BY_USERNAME, (username,))

    record = cursor.fetchone()
    return  record

def get_job(profile_id):
    cursor.execute(sql_query.FETCH_JOB_BY_PROFILE_ID, (profile_id,))

    record = cursor.fetchall()
    return record

def add_new_data(data):
    cursor.execute(sql_query.INSERT_PROFILE, (data["name"], data["username"], data["password"]))
    
    connection.commit()
    return

def get_user_id():
    cursor.execute(sql_query.FETCH_ALL_USER_ID)

    record = cursor.fetchall()
    return  record
