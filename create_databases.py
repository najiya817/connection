import mysql.connector

conn = mysql.connector.connect(user='root', password='abc123', host='127.0.0.1')

cursor = conn.cursor()

cursor.execute("drop database if exists mydatabase")

sql="create database mydatabase"

cursor.execute(sql)

print("list of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

conn.close()