list=[]
list1=[]
list2=[]
total=[]
n = int(input("How many items in your shopping list?"))
for i in range(0, n):
    item = input("Enter name of Item:")
    quantity = int(input("Enter quantity:"))
    price = int(input("Enter price:"))
    list.append(item)
    list1.append(quantity)
    list2.append(price)
for i in range(0, len(list1)):
    val = (list1[i] * list2[i])
    total.append(val)
Bill=sum(total)
print("Total bill amount is :{}".format(Bill))
