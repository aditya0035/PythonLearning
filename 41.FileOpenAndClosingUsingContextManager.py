"""
We can open and close a file automatically as File class already implemented context manager so we can use it
with keyword
the with keyword automatically call __enter__ and __exit__ when code completed the context manager
"""
"""
Using with keyword
1.setup(open) and teardown(close) approch
2.it is less error prone like using in C#
3.also kown as context manager so those classes which have implemented __enter__,__exit__ method we can use them with keyword
4.it is also used for sql connection manager
"""
with open("dummy.txt","r") as filePointer:
    while True:
        line=filePointer.readline()
        if not line:
            break
        print(line)


'''
Here we didn't explicitly closes the file it will automatically closes once code execution under the block completed
'''
        