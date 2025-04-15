import sqlite3

# connect to sqlite
connection=sqlite3.connect("student.db")


# create a cursor object to insert record , create table,retrieve
cursor=connection.cursor()


# create the table

table_info="""

Create table STUDENT 
(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

# insert some more records

cursor.execute('''
Insert into STUDENT values ('Sahil','Data science' ,'A',90)
''')
cursor.execute('''
Insert into STUDENT values ('Sumit','Data science' ,'B',70)
''')
cursor.execute('''
Insert into STUDENT values ('Pawan','Data Analytics' ,'A',85)
''')
cursor.execute('''
Insert into STUDENT values ('Dhruv','Data science' ,'A',90)
''')
cursor.execute('''
Insert into STUDENT values ('Ashish','Machine Learning' ,'B',60)
''')

# display the records

print("The inserted records are")

data=cursor.execute('''
select * from STUDENT''')

for row in data:
    print(row)

## close the connection

connection.commit()
connection.close()