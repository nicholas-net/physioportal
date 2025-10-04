import psycopg2

try:
    conn = psycopg2.connect("dbname=physio user=clinic_user password=MyPassword123 host=localhost")
except:
    print("Unable to connect to database")

with conn.cursor() as cur:
    try:
        cur.execute("""CREATE TABLE patients (patient_id SERIAL PRIMARY KEY, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, 
            date_of_birth DATE NOT NULL,  medical_history VARCHAR(255));""")
        conn.commit()
        conn.close()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
