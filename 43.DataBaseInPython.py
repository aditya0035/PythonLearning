"""
python provide inbuiit database module to deal with database which is sqllite3
but it support one write operation but multiple read operation at a time
"""
"""

To work with database in python there are three steps.
1.Create Connection Object
2.Get Cursor for perfroming operation on database
3.Commit the changes from connection
4.close the connection

In python we use cursor not connection because if we use connection object for 
reading and writing then we can perfrom one operation but using cursor we can perform 
read as well as write operation under the same connection

Python comes with inbuilt module to deal with Sqllite3
its not a global module so we have to import that

SqlLite3 support following datatypes
1.NULL
2.Integer
3.Float
4.Text
5.Blob (binary datatype for images dealing)
"""
import sqlite3

class Connection:
    def __init__(self,database_name):
        self.database_name=database_name
    def CreateTable(self):
        con=sqlite3.connect("data.db")
        cursor=con.cursor();
        cursor.execute("create table employee if not exists(id integer,name Text")
        con.commit()
        con.close()
    def InsertEmployeeData(self,id,name):
        conn=sqlite3.connect("data.db")
        cursor=conn.cursor()
        cursor.execute(f"insert into employee(id,integer) values({id},'{name}') ")
        #above query is sql injection prone so we have to write in another way
        conn.commit()
        conn.close()
    def FindEmployee(self,name):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.fetchall("Select * from employee where name=?",name)
        conn.commit()#it will commit all the trasaction happened over this connection
        conn.close()
        #when we commit the changes then it will save otherwise it will be RAM
    def UpdateEmpName(self,oldname,newname):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("Update employee set name=? where name=?",newname,oldname)
        conn.commit()
        conn.close()
    def GetAllEmployees(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.fetchall("Select * from employee order by name desc")
        conn.commit() #here commit has no meaning as no DDL/DML(update,delete,Insert) operation performed
        conn.close()
    def GetTopNEmployee(self,noOfEmp):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.fetchall("Select * from employee order by name limit ?",noOfEmp)
        conn.close();

"""
In Python we have various driver availiable online to work with other db 
we need to install them using pip and then write the query as we write above
"""