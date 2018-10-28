fruits={"Orange":"sweet and sour fruit","Apple":"Good for health","Lemon":"Has vitamin C","Carrot":"Has Vitamin A"}
name=input("what do you want")
print(fruits[name])#dictname[key]gives value
print(fruits.get(name))#will not give error if key not in dictionary, output will be none
if name in fruits:
    print(fruits[name])
else:
    print("fruits not found")
if fruits.get(name)!=None:
    print(fruits.get(name))

