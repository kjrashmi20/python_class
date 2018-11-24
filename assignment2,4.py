Phonebook={}
Name=[]
Number=[]
print("1.Add a contact")
print("2.Delete a contact")
print("3.Search a contact")
print("4.Print the Phonebook")
wish=int(input("Select option"))
for i in range (1,4):
    if wish==1:
        name=input("Enter contact name")
        num=int(input("Enter contact number"))
        Phonebook[name]=num
        print(Phonebook)
    elif wish==2:
        name = input("Enter contact name")
        num = int(input("Enter contact number"))

    elif wish==3:
        num= input("Enter contact number")
        if num in Number:
            print("contact found")
        else:
            print("contact not found")









