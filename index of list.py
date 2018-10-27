mylist=["Horse","Wild boar","Sheep","Tiger"]
ind=mylist.index("Tiger")#finding index
print(ind)
mylist.remove("Sheep")#remove an element
print(mylist)
ind=mylist.index("Tiger")
print(ind)
del mylist[0]#remove element id index is known
print(mylist)
# del mylist will delete complete list
print("*"*60)
list1=[1,2,3]
list2=list1
del list1
print(list2[0])
