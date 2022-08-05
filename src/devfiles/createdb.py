import sqlite3
connection_obj = sqlite3.connect('sharecodes.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS SHARECODE")
cursor_obj.execute("DROP TABLE IF EXISTS SCHASH")
table = """ CREATE TABLE SHARECODE (
            Sharecode INT,
            ModelJson CHAR(100) NOT NULL
        ); """
cursor_obj.execute(table)
table = """ CREATE TABLE SCHASH (
            Sharecode INT,
            Hash CHAR(100) NOT NULL
        ); """
cursor_obj.execute(table)
print("ShareCode DB Is Ready, saved to sharecodes.db")
connection_obj.close()