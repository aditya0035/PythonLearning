numb=int(input("Enter a number \n"))

for i in range(0,numb):
    print(f"Welcome to python count:{i}")

primes=[2,3,5,7]
for i in primes:
    print(f"Prime Number are :{i}")

kid_age=(10,15,19)
for age in kid_age:
    print(f"my kid age is {age}")

#here both list and kid age are iterables that is we can use for on that
#Range is not a iterable its a genrator with iterable functionality which i will explain later
print(range(12))

#iteration over dict
my_friends={
    "Joe":6,
    "Jack":15,
    "Rajesh":18,
    "Alex":20
}

for key in my_friends:
    print(f"I didn't meet {key} since {my_friends[key]} days")

print(my_friends.items())

dic_item=my_friends.items();

lst_dic_item=list(dic_item)

for item in lst_dic_item:
    print(f"I didn't meet{item[0]} since {item[1]} days")

print("tuple Destructuring")

for key,value in lst_dic_item:
    print(f'i didn;t meet {key} since {value} days')


a,b,c=11,12,13
print(f'a:{a}, b:{b}, c:{c}')