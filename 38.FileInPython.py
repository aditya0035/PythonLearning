"""
To deal with file we have following method
1.open("<file name,if file at other location then absolute path>","File Operning mode")
there are below 
1.a append mode will append text at the end
2.r read mode this will read the file
3.w write mode this will truncate the file and add content at the from beganining
4.r+ opens for reading and writing (no truncating, file pointer at the beginning)
5.w+ opens for writing (and thus truncates the file) and reading
6.a+ opens for appending (writing without truncating, only at the 
end of the file, and the file pointer is at the end of the file) and reading
once we open a file it will return a file pointer by that we can read the content of file
apart from mode we can read the file in text and binary mode default is text mode
for bindary use rb b for binary

once we are done with file we have to close the file as we have limited number of resouces to work with
"""
filePointer=open("38.filepython.txt",'w') #it will open file in write mode
filePointer.write("Welcome to python line 1")
filePointer.write("\nWelcome to python line2")
filePointer.close()

filePointer=open("38.filepython.txt","r")
'''for line in filePointer.readlines():
    print(line)
'''
while  True :
    line=filePointer.readline()
    print (line)
    if not line:
        break
filePointer.close()


"""
When we open a file in write mode it will earse the content of file and will start writing to the file from starting
it sometime happens that when we read a file it will conatins \n \t (new line or tab or white spaces) so to deal with we have to first Trim using strip() that text
so that it will remove the spaces from that and provide text without tab or new line character

"We can use split function to split the lines based on some delimiter"
"""