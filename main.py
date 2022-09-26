import sqlite3
import os
import platform

db = sqlite3.connect("device.db")
cur = db.cursor()
liste = cur.fetchall()

cur.execute("""CREATE TABLE IF NOT EXISTS DEVICE (
Hostname nvarchar
);""")


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
            raise Exception("Error occurs")


        elif len(self.DeviceName) == 15:
            print("Hostname available!")

        cur.execute("INSERT INTO DEVICE (Hostname) VALUES (?)", (Hostname,))

Environment("Hostname")

