list=[2,4,6]
list2=[6,2,4]
if(list==sorted(list2)):
    print("lists are equal")
else:
    print("lists are not equal")
list3=[2,4,6]
if(list is list3):
    print("Address space is equal")
else:
    print("Address space not equal")

list3=list
list3.append(8)
print(list)

