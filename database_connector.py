import pymysql
import sqlalchemy
from google.cloud.sql.connector import Connector
import os
username=os.getlogin()
import google.auth
import pandas as pd
from datetime import datetime, timedelta
today=datetime.today().strftime('%Y-%m-%d')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'db_creds/myfootpath-database-ef917cb06b4c.json'
def database_connection():
    # initialize Connector object
    connector = Connector()

    # function to return the database connection
    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            "myfootpath-database:us-central1:mysql-myfootpath",
            "pymysql",
            user="root",
            password="m%F00tp47h",
            db="myfootpath-database"
        )
        return conn

    # create connection pool
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://?charset=utf8mb4",
        creator=getconn,
    )
    #print(pool.execute("ALTER DATABASE myfootpath-database CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;").fetchall())
    return pool
#df=pd.read_csv('C:/Users/GS/Google-Api-Stuff/completion.csv')
#df.to_sql('users',con=pool,index=False)
#database_connection()
##insert_stmt = sqlalchemy.text(
##    "CREATE TABLE testtable (cat int)",
##)
##
##with pool.connect() as db_conn:
##    # insert into database
##    db_conn.execute(insert_stmt)
##
##    # query database
##    result = db_conn.execute("SELECT * from my_table").fetchall()
##
##    # Do something with the results
##    for row in result:
##        print(row)
