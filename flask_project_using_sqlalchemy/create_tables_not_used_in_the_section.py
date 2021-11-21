import sqlite3
from threading import currentThread 
 
connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
cursor = connection.cursor() 

create_table = "create table if not exists users (id integer primary key, username text, password text)" 
cursor.execute(create_table)  

create_table = "create table if not exists items (id integer primary key, name text, price real)" #real is just value with decimal point
cursor.execute(create_table) 

connection.commit() 
connection.close() 
