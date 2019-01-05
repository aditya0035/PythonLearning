def Read_CSV_File():
    file_pointer=open('CSV.txt','r')
    content=file_pointer.readlines()
    content=[content.strip()for content in content]
    file_pointer.close()
    header=(item.split(',') for item in content[0:1])
    rest_content=content[1:]
    header=next(header)
    print(rest_content)
    content_dict={}
    for i,item in enumerate(rest_content):
       content_dict[f'{i}']=dict(zip(header,item.split(',')))
    print(content_dict)

Read_CSV_File()