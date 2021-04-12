DB_HOST = "localhost"
DB_NAME = "web_telemovel"
DB_USER = "postgres"
DB_PASS = "cisco"
DB_PORT = "5432"

import psycopg2
conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER, password=DB_PASS, host=DB_HOST)





