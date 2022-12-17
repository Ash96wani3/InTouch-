import mysql.connector
mycon=mysql.connector.connect(host='local host',user='root',passwd='parvathy')
mycur=mycon.cursor()
try:
 sql="create database intouch"
 mycur.execute(sql)
except:
 print("DATABASE ALREADY CREATED")
mycur.execute("use intouch")

p="create table elder_details(Name varchar(50),Age int,Gender varchar(15),Nationality varchar(20),Address varchar(55),Contact Number int)"
mycur.execute(p)