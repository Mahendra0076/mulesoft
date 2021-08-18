# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(host='localhost',database='training',user='root', password='')
#     if connection.is_connected():
#             db_Info = connection.get_server_info()
#             print("Connected to MySQL Server version ", db_Info)
#             Cursor = connection.cursor()
#             record = Cursor.execute("select * from movies")
#             record = Cursor.fetchall()
#             print(record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         Cursor.close()
#         connection.close()
#         print("MySQL connection is closed")







import pymysql
import pandas as pd

dbcon = pymysql.connect(host="localhost", user="root", password="", database="training")

try:
    SQL_Query = pd.read_sql_query(
        "select * from movies", dbcon)
    df = pd.DataFrame(SQL_Query)
    print(df)
    # print(SQL_Query)
except :
    print("Error")