'''1.Counter it will count no of ocuurence of all the element in a list as dict'''
from collections import Counter,defaultdict,OrderedDict,namedtuple,deque
lst=[1,2,3,41,1,5,1,6,1]
print(Counter(lst))

'''2.default dic:it will behave like dict but the things is when we try to access an element
which is not in the list we get errror and also we want some logic that if its empty the it should
return something some which we can work'''
dic={
    "Jim":[90,95,92,93,91],
    "Kim":[65,70,84,99,98],
    "Alex":[68,69,72,78,85]
}

dft_dict=defaultdict(**dic)
dft_dict.default_factory=list #"Here we have specified that default value should be []"
print(dft_dict)

lst=dft_dict["Jack"]
lst.append(90)
lst.append(98)
lst.append(100)
lst.append(55)
lst.append(93)
print(dft_dict)
#if a element does not exist it will give default value provided using factory and then add that key into the dic

'''3.Ordered Dict:it is the dictionary which maintained there order in future it will obslete and this
functionality will be included as a part of dictionary
'''
ordered_dict=OrderedDict(**dic)
print(ordered_dict)

'''4.Named tuple are the tuple having for each element they have
for named tuple we have to define the schema first
'''

users_tuple=namedtuple("users_tuple",["username","password"])
tuple_value= users_tuple(username="jim",password="123")
name,password=tuple_value.username,tuple_value.password
print(name)
print(password)
print(tuple_value._asdict()) #this convert existing tuple to dictionary

'''5.Dequeue is thread safe its like a list where we can do operation from both end in deque we are passing iterable
which then covert one by one into deque object'''
friends=deque(["jack","jim"])
print(friends)
friends.append("Kim")
print(friends)
friends.appendleft("Jimmy")
print(friends)
friends.pop()
print(friends)
friends.popleft()
print(friends)