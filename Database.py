#Q.1- Write a python script to create a database of students named Students.
import sqlite3
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = 'create table students(name varchar(20),roll_no int(10), age int(2), marks int(3))'
    cursor.execute(query)
    print('Table created successfully!!')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')


#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = 'create table students(name varchar(20),roll_no int(10) primary key, marks int(3))'
    cursor.execute(query)
    con.commit()
    print('Table created successfully!!')
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')
record=[]
i=0
while(i<10):
    try:
        name=input("Enter name: ")
        marks=int(input('Enter marks: '))
        if(marks<0 or marks >100):
            raise ValueError('Invalid marks')
            i=i-1
        else:
            t=name,marks
            record.append(t)
            i=i+1
    except  ValueError as v:
        print(v)

        
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = "insert into students(name, marks) values(?,?)"
    records =record
    cursor.executemany(query, records)
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')


#Q.4- Print the names of all the students who scored more than 80 marks.
import sqlite3
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = 'select * from students where marks>80'
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print('Name: {}'.format(row[0]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')
