customers={}
cust1=["Mukund",20,"HSR",{
    1:[[444,"moto e4",10000,1],[555,"black shirt",1000,4],[666,"TV",20000,1]],#first transcation
    2:[[222,"cricket bat",400,3],[777,"tennis bat",167,1]]},"prime"]#second transaction
cust2=["Dravid",29,"Kormangala",{
    1:[[404,"Samsung",10000,1],[505,"White shirt",1000,4],[606,"Camera",20000,1]],#first transaction
    2:[[222,"cricket kit",4000,3],[777,"Skipping rope",167,1]],#second transaction
    3:[[678,"Sofa Set",50000,1]]},"not prime"]#third transaction
customers[9972542698]=cust1# adding to empty dict customers
customers[9987356472]=cust2
print(customers)
phonenum=int(input("Enter phone number:"))
shoppinglistkey1=1
if phonenum in customers:
    shoppingdict=customers[phonenum][3]
    if shoppinglistkey1 in shoppingdict:
        item1=shoppingdict[shoppinglistkey1]
        print(item1[0][1])
    else:
        print("You have never shopped with us before, you have exciting offers for you")
else:
    print("Sorry couldn't find your details, please create an account with us")






