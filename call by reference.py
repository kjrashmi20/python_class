def addToList(l,item):
    l.append(item)
def deleteFromitem(l,item):
    l.remove(item)
def printList(l):
    for item in l:
        print(item)
def findElement(l,item):
    if item in l:
        print("Item found at index{}".format(l.index(item)))
    else:
        print("Item not found")

shopping_list=[]
while(True):
    print("1.Add")
    print("2.Delete")
    print("3.Print List")
    print("4.Print item")
    print("-1 to exit")

    choice=int(input("what u want"))
    if(choice==-1):
        break;
    if(choice==1):
        item=input("Enter name:")
        addToList(shopping_list)
    if (choice == 2):
        item = input("Enter name:")
        deleteFromitem(shopping_list)







