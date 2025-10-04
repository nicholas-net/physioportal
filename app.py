import psycopg2

try:
    conn = psycopg2.connect("dbname=physio user=clinic_user password=MyPassword123 host=localhost")
except:
    print("Unable to connect to database")

with conn.cursor() as cur:
    try:
        cur.execute("""CREATE TABLE users (user_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, 
            date_created TIMESTAMP NOT NULL DEFAULT(CURRENT_TIMESTAMP), last_updated TIMESTAMP NOT NULL DEFAULT(CURRENT_TIMESTAMP));""")
        conn.commit()
        conn.close()
        cur.close()
        print("Query executed")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

