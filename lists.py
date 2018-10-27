fruits=[]
while True:
    fruit=input("enter a fruit")
    if(fruit=="exit"):
        break;
    fruits.append(fruit)
item=input("Which fruit are you looking for")
if item in fruits:
        print("Fruit is available")
else:
        print("Fruit is not available")