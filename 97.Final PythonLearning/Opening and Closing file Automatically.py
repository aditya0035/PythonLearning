'''in this module i will tell how to open and close file automatically
this thing is done by context manger which excute in such a way that once the context of the block of
code is about to exist it will close the file automatically we didn't need to explicitly close the file
for context manager handling we use with keyword
'''

def automatically_close_file():
    try:
        with open("demo.txt",'r') as file_pointer:
            content=file_pointer.readlines()
            for item in content:
                print(item)
    finally:
        if not file_pointer.closed:
            file_pointer.close()
            print("file is now closed")

automatically_close_file()