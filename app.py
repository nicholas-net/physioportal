import psycopg2

try:
    conn = psycopg2.connect("dbname=physio user=clinic_user password=MyPassword123 host=localhost")
except:
    print("Unable to connect to database")

with conn.cursor() as cur:
    try:
        cur.execute("""ALTER TABLE patient_programs 
            ADD COLUMN IF NOT EXISTS reps INTEGER NOT NULL""")
        conn.commit()
        conn.close()
        cur.close()
        print("Query executed")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# Fix patient progarm table . add sets, reps