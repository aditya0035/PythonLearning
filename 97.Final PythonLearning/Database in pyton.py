import  sqlite3
class ConnectionManager:
    '''to implement a context manager we need to implement __enter__ and __exit__ method
    __enter__ method provide the object
    __exit__ will do the formality
    its has various argument which play role in exception handling
    '''
    def __init__(self,database_name):
        self.database_name=database_name
    def __enter__(self):
        '''in this method we are going to return the connection object'''
        self.connection=sqlite3.connect(self.database_name)
        return self.connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''this method will close the connection also it might happen that while performing
        operation in context manager some exception occurs then the call will come here with all the details
        like exception type ,exception value,exception traceback, so if developer want to do something on the message
        he can do that and if exception is gracefully handled in this method then it hase to retur True value
        if no value is return from here then exception will re raise automatically from here after executing its code
        will goes till it handle or will crash the program
        any db related problem solve into three parts
        1.create connection
        2.fetch connection object
        3.Get Cursor object from connection object
        4.Commit the changes on connection object
        5.Close the connection
        Sqllite3 support only one write @ a time and multiple read
        Instead of connection cursors are used as cursor support multiple read and write simultaneously
        with each run the data is not deleted from db files
        '''
        self.connection.commit()
        self.connection.close()

class Query:
    def __init__(self,dbname):
        self.dbname=dbname

    def create_table(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("Create table if not exists emp (id integer,name text)")

    def insert_data(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("insert into emp(id,name) values(?,?)",(1,'Aditya'))
            '''
            here we have used ? although we can use format string but the issue with format string
            is that there is chance of SQL injection to avoid that we write the query in this format
            '''
    def fecth_data(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("Select * from emp")
            empdata=cursor.fetchall()
            print(empdata)

    def update_data(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("update emp set name=? where name=?",("Saraswat","Aditya"))

    def delete_data(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("delete from emp where name=?",("Aditya",))

    def fetch_data_where(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("Select * from emp where id=?",1)
            result= cursor.fetchall()
            print(result)
    def fetch_data_order(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.cursor()
            cursor.execute("select * from emp order by name desc") #default is asc(ascending)
            result=cursor.fetchall()
            print(result)

    def fetch_data_limit(self):
        with ConnectionManager(self.dbname) as connection:
            cursor=connection.execute("Select * from emp limit 1")
            result=cursor.fetchall()
            print(result)

def Main():
    if __name__=='__main__':
        print("in if")
        query=Query('db')
        query.create_table()
        query.insert_data()
        query.fecth_data()
        query.update_data()

Main()