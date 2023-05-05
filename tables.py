
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="library")
print(mydb)
myc=mydb.cursor()
myc.execute('''create table books (Book_code integer(5) NOT NULL PRIMARY KEY,'''
            '''Book_name varchar(20) NOT NULL, Author varchar(20) NOT NULL,'''
            '''Publisher varchar(20) NOT NULL, QTY integer(3) NOT NULL)''')

myc.execute('''create table issue (Reg_no integer(5) NOT NULL PRIMARY KEY,'''
            '''Reciever_name varchar(30) NOT NULL ,Book_code integer(5) NOT NULL,'''
            '''Date_of_issue date NOT NULL , submit_date date , Submit char(8))''')

mydb.commit()
print( "tables created ")
