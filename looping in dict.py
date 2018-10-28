#looping using keys and values
fruits={"Orange":"sweet and sour fruit","Apple":"Good for health","Lemon":"Has vitamin C","Carrot":"Has Vitamin A"}
for key in fruits:#prints key and values
    print("{}:{}".format(key,fruits[key]))
print("*"*60)
for val in fruits.values():#prints values
    print(val)
for key,val in fruits.items():#prints key and values
    print(key)
    print(val)