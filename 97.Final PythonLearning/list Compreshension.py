'''List comprehension is creating a lsit using an expression,loop and condition'''
list1=[numb for numb in range(10)]
print(list1)

square_list=[numb**2  for numb in range(10)]

print(square_list)

square_list_even=[numb**2  for numb in range(10) if numb%2==0]
print(square_list_even)

