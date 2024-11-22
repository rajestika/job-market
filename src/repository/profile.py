from apps.src.main import cursor, connection

def get_data_based_on_username(username):
    cursor.execute("""SELECT
                   p.id,
                   p.name,
                   p.username,
                   p.password                 

                   from profile p

                   where p.username = %s""", (username,))

    record = cursor.fetchone()
    return  record

def get_job(profile_id):
    cursor.execute("""SELECT
                   j.name,
                   j.description as desc,
                   j.gaji

                   from job j

                   join profile_job pj on j.id = pj.job_id

                   where pj.profile_id = %s""", (profile_id,))
    record = cursor.fetchall()
    return record

def add_new_data(data):
    cursor.execute("INSERT INTO profile (name, username, password) VALUES (%s, %s, %s)", 
            (data["name"], data["username"], data["password"]))
    connection.commit()
    return

def get_user_id():
    cursor.execute("""SELECT
                   p.id
                   
                   from profile p
                   """)

    record = cursor.fetchall()
    return  record
