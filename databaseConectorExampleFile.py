# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:49:36 2022

@author: DianaValladares
"""
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, tools
from oauth2client import  client as c
from scripts.recent_file import recent_file
import database_connector as db_c
import pandas as pd
import numpy as np
import regex as re
import time
import os

username=os.getlogin()
pool=db_c.database_connection()


''' Example Uploading '''
# =============================================================================
#
#    from scripts.recent_file import recent_file
#
#    not_enrolled_df=pd.read_csv(not_enrolled)
#    not_enrolled_df.to_sql('not_enrolled_daily',con=pool,index=False,if_exists='replace')
# 
#    df = pd.read_csv(recent_file("C:/Users/DianaValladares/Downloads/Workflow-Runs-22-Aug-2022" , ".csv" , 1))
#
#
# =============================================================================
# Database Connector to Connect Google Cloud Console to a Python Script 
# =============================================================================
# import pymysql
# import sqlalchemy
# from google.cloud.sql.connector import Connector
# import os
# username=os.getlogin()
# import google.auth
# import pandas as pd
# from datetime import datetime, timedelta
# today=datetime.today().strftime('%Y-%m-%d')
# 
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'db_creds/myfootpath-database-ef917cb06b4c.json'
# def database_connection():
#     # initialize Connector object
#     connector = Connector()
# 
#     # function to return the database connection
#     def getconn() -> pymysql.connections.Connection:
#         conn: pymysql.connections.Connection = connector.connect(
#             "myfootpath-database:us-central1:mysql-myfootpath",
#             "pymysql",
#             user="root",
#             password="m%F00tp47h",
#             db="myfootpath-database"
#         )
#         return conn
# 
#     # create connection pool
#     pool = sqlalchemy.create_engine(
#         "mysql+pymysql://?charset=utf8mb4",
#         creator=getconn,
#     )
#     #print(pool.execute("ALTER DATABASE myfootpath-database CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;").fetchall())
#     return pool
# =============================================================================

df = pd.read_csv(recent_file("C:/Users/DianaValladares/Downloads/Workflow-Runs-22-Aug-2022" , ".csv" , 1))
df2 = df[['Summary', 'Workflow name']]
df2 = df2.head()

df2.to_sql("Workflow Runs", con=pool, index=False, if_exists='replace')

old_name = "C:/Users/DianaValladares/Desktop/Analyst/BoxSync/toBoxSync.py"
new_name = "C:/Users/DianaValladares/Desktop/Analyst/BoxSync/databaseConectorExampleFile.py"

os.rename(old_name, new_name)