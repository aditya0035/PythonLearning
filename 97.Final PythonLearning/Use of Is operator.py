'''the difference b/w == and is that == check for content and is check for id i.e whater they are same object'''
list1=[23,24,25,26,27]
list2=[23,24,25,26,27]
list3=list2
list4=[23,24,25,26,27,28]
if list1==list2:
    print("both list are equal")

if list1 is list2:
    print("both list point to same object")

if list1==list4:
    print("list 1 and list4 both have same content")

if list2 is list3:
    print("both list point to same location")