my_friends=["Jim","Kim","Joe","Jack","Jim"]
friend_name=input("Please give friend name")
index=0;
for name in my_friends:
    if(name==friend_name):
        break;
    else:
        index+=1

print(f"friend is present at index {index}")

lst_of_numb=[1,2,3,4,5,6,7]
odd_num_lst=[]
for numb in lst_of_numb:
    if numb%2!=0:
        odd_num_lst.append(numb)
    else:
        print("even number")
        continue
        print("custom message")

print(odd_num_lst)

#no iteration will happen here
for i in range(2,2):
    print(i)