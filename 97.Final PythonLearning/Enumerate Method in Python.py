tpl=['jack','joe','jimmy','donald']
age=[19,34,65,25]
'''
for i,name in enumerate(tpl):
    print(f'Name:{name} & Age:{age[i]}')
    
here enumerate this is the start index so for mismatching of sequences we can set up own index
'''
for i, name in enumerate(tpl,1):
    print(f'Index:{i}  Name:{name} & Age:{age[i]}')