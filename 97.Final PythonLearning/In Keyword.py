my_friends=["joe","Jack","kim"]
my_friends_dic={
    0:"jack",
    1:"James",
    2:"Kim"
}

if 'kim' in my_friends:
    print("Kim found")
if 'kim' in my_friends_dic: #here it search on key
    print("kim is in dict")
if 1 in my_friends_dic:
    print("index 1 is there")
