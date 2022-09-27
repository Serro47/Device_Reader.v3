import sqlite3
import os
import platform
import mysql.connector
from mysql.connector import Error


class Environment:
    def __init__(self, Hostname):
        self.Username = os.getlogin()
        self.DeviceName = (platform.node())
        print(f"Environment: {self.DeviceName[0:1]}")
        print(f"location: {self.DeviceName[1:4]}")
        print(f"GSSN: {self.DeviceName[4:11]}")
        print(f"Devicetype: {self.DeviceName[11:13]}")
        print(f"Devicenumber: {self.DeviceName[13:15]}")

        if len(self.DeviceName) != 15:
            print("----------------------")
            print("Hostname not available!")


        elif len(self.DeviceName) == 15:
            print("Hostname available!")


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='devicedb',
                                         user='root',
                                         password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
    print("MySQL connection is closed")
    print("----------------------")

Environment("Hostname")
