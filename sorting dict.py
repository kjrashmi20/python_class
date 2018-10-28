fruits={"Orange":"sweet and sour fruit","Apple":"Good for health","Lemon":"Has vitamin C","Carrot":"Has Vitamin A"}
print(fruits.keys())
print(fruits.values())
listofkeys=list(fruits.keys())
listofvalues=list(fruits.values())
print(listofkeys)
print(listofvalues)
newkeys=sorted(listofkeys)
newval=sorted(listofvalues)
print(newkeys)
print(newval)
for key in newkeys:
    print("{}:{}".format(key,fruits[key]))