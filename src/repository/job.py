from apps.src.main import cursor, connection

def get_job_list():
    cursor.execute("""SELECT
                   j.name as job_name,
                   j.description as desc,
                   j.gaji

                   from job j""")
    record = cursor.fetchall()
    return record

def get_job(job_name):
    cursor.execute("""SELECT
                   j.name,
                   j.description as desc,
                   j.gaji

                   from job j
                   
                   where j.name = %s""", (job_name,))
    record = cursor.fetchone()
    return record

def add_job(data):
    cursor.execute("INSERT INTO job (name, description, gaji) VALUES (%s, %s, %s)", 
            (data["job_name"], data["desc"], data["gaji"]))
    connection.commit()
    return

def add_application(data):
    cursor.execute("INSERT INTO profile_job (profile_id, job_id) VALUES (%s, %s)", 
            (data["user_id"], data["job_id"]))
    connection.commit()
    return

def get_job_name(job_id):
    cursor.execute("""SELECT
                   j.name
                
                   from job j
                   
                   where j.id = %s""", (job_id,))
    record = cursor.fetchone()
    return record

def get_job_id():
    cursor.execute("""SELECT
                   j.id
                
                   from job j
                   """)
    record = cursor.fetchall()
    return record