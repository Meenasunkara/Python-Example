import pandas as pd
Automobile_data = pd.read_csv('C:\\Users\\meena\\Downloads\\Automobile_data.csv', index_col=False, delimiter = ',')
#print
Automobile_data .head()
#empdata = pd.read_csv('C:\\Users\\meena\\Downloads\\us-500\\empdata.csv', index_col=False, delimiter = ',')
#empdata.head()


import mysql.connector as msql
from mysql.connector import Error



try:
    conn = msql.connect(host='localhost', database='automobiledatabase', user='root', password='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS table_1;')
        print('Creating table....')
# in the below line please pass the creation table statement which you want #to create
        cursor.execute("CREATE TABLE table_1 (s_no int,company varchar(255),body_style varchar(255),wheel_base int,length int,engine_type varchar(255),num_of_cylinders varchar(255),horsepower int,average_mileage int,price int)")
        print("Table is created....")
        #loop through the data frame
        for i,row in Automobile_data.iterrows():
            #here %S means string values
            sql = "INSERT INTO automobiledatabase.table_1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()

except Error as e:
            print("Error while connecting to MySQL", e)