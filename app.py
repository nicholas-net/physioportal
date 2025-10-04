import psycopg2

try:
    conn = psycopg2.connect("dbname=physio user=clinic_user password=MyPassword123 host=localhost")
except:
    print("Unable to connect to database")

with conn.cursor() as cur:
    try:
        cur.execute("""CREATE TABLE patient_programs (program_id SERIAL PRIMARY KEY, patient_id INTEGER REFERENCES patients(patient_id), 
        exercise_id INTEGER REFERENCES exercises(exercise_id));""")
        conn.commit()
        conn.close()
        cur.close()
        print("Query executed")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
