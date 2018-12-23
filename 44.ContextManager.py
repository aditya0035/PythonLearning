"""
To create context manager we have to implement __enter__ and __exit__ method
and __exit__ method is responsiable for exception handling
"""
import sqlite3
c
lass ConnectionManager:
    def __init__(self,databaseName):
        self.databaseName=databaseName;
    def __enter__(self):
        connection=sqlite3.connect(self.databaseName)
        self.connection=connection
        return connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Here below parameter mead
        :param exc_type: Exception Type
        :param exc_val: Exception Value
        :param exc_tb: Exception trace back
        :return: it is the value which is to be return if it is return None that will
        propogate the exception if it is return true then the exception will be swallow by this block
        it is helpful when there is an exception occurs in the context manager
        """
        self.connection.commit()
        self.connection.close()


with ConnectionManager("Data.db") as connectionManager:
    cursor=connectionManager.cursor()
    cursor.execute("Select* from employee")

