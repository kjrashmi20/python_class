list=[]
list1=[]
for i in range (1,11):
    n=int(input("Enter number:"))
    list.append(n)
print(list)
for i in range (0,len(list)):
    if list[i]%5==0 and list[i]%2==0 and list[i]%3!=0:
        list1.append(list[i])
list2=sorted(list1)
print("Numbers in sorted order divisible by 5 and 2 but not by 3 are:")
for item in list2:
    print(item)






