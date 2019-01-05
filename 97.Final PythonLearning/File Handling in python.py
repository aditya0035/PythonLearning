'''
In python we use open to open a file which return afile handler which then we can use to do various operation
open method takes two argument 1st is the file path with name and args to is the mode
there are 4 modes
1.r:read only mode
2.w:write mode in this file will be created if not exists and each time previous content will be deleted and oerride it with new content
3.a:open the file in append mode that is if file not exists will create and write the file if file is already there it
will start writing the file form the last line pointer and append the content from that
4.r+:open the file in read and write mode
When we close the file then it goes to write the content in the file other wise the content is in RAM
Close function is use to close the file
apart from  there are two way in which we can read or write the files
1.Text:it is default and is human readable format
2.binary:this is used to store image data or binary data format
use rb read binary
wb write binary
once you are done with your operation please close tha file as os has limitation to open a no of file instances
'''
def working_with_file():
    file_pointer=open('demo.txt','w')
    file_pointer.write("This is my line")
    file_pointer.close()

    file_pointer=open('demo.txt','r')
    content=file_pointer.readlines()
    file_pointer.close()
    for line in content:
        print(line)
    del content #used to relase memory
    file_pointer=open('demo.txt','r')
    file_pointer.seek(0)  # reset the file pointer to begaining but used when we are not closing the file once close the file it reste the pointer
    content=file_pointer.readlines()
    print(f'second time :\n{content}') #no content as pointer or cursor is at last
    file_pointer.close()
    file_pointer = open('demo.txt', 'r')
    content=file_pointer.readline()
    print(f'Third time :\n{content}')
    file_pointer.close()
    file_pointer=open('demo.txt','a')
    file_pointer.write("\nThis is another line")
    file_pointer.close()

    '''Working of file.readlines function and readline4444444444444444dddddddddddddddd'''
    file_pointer=open('demo.txt','r')
    content= file_pointer.readlines()
    print(content)
    content=[line.strip() for line in content] #strip function remove all white spaces ,tab,and new lines
    print(content)
    lineIterator=content.__iter__()
    print(next(lineIterator))
    print(next(lineIterator))
'''split() function genrally split the string based on provided charater usulally we prefer
# Or , as separtor
'''


working_with_file()