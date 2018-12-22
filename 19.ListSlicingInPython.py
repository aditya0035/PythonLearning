my_list=["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Chandigarh","Dadra and Nagar Haveli"]
"""
in lit slicing we will create a sublist using Slicing Operator
perform using [startindex:end index:difference]
default startindex=0
default endindex=length
difference=0
for negative index it will start from end -1 to -last 
and travel from left to right while picking element
"""
sub_list=my_list[:3]
print(sub_list)
print(my_list[0:len(my_list):2])
print(my_list[-3:-5])
print(my_list[-5:-3])

