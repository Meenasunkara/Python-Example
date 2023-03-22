import mysql
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',
                        password='root')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE automobiledatabase")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)