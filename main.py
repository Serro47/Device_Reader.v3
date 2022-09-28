import sqlite3
import os
import platform
import mysql.connector
from mysql.connector import Error


class Environment:
    def __init__(self, Hostname):
        self.Username = os.getlogin()
        self.DeviceName = (platform.node())
        self.env = self.DeviceName[0:1]
        self.location = self.DeviceName[1:4]
        self.gssn = self.DeviceName[4:11]
        self.devicetype = self.DeviceName[11:13]
        self.devicenumber = self.DeviceName[13:15]

        print(f"Environment: {self.env}")
        print(f"location: {self.location}")
        print(f"GSSN: {self.gssn}")
        print(f"Devicetype: {self.devicetype}")
        print(f"Devicenumber: {self.devicenumber}")

        if len(self.DeviceName) != 15:
            print("----------------------")
            print("Hostname not available!")

        elif len(self.DeviceName) == 15:
            print("Hostname available!")


device = Environment("Hostname")

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
        sql = "INSERT INTO device (environment, location, gssn, devicetype, devicenumber) VALUE (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (device.env, device.location, device.gssn, device.devicetype, device.devicenumber))
        connection.commit()
        cursor.close()
        connection.close()
    print("MySQL connection is closed")
    print("----------------------")
