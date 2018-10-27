menu=[]
dish1=[1,"Egg curry",84.5,["egg","onion","chilly"]]
dish2=[2,"Egg pasta",44.5,["egg","noodles","cheese"]]
dish3=[3,"Mashed potato",34.5,["potato","onion","chilly"]]
dish4=[4,"salad",20.5,["carrot","onion","cucumber"]]
dish5=[5,"Roti curry",14.5,["wheat","onion","chilly"]]
menu.append(dish1)
menu.append(dish2)
menu.append(dish3)
menu.append(dish4)
menu.append(dish5)
item=input("Please enter what you like")
for dish in menu:
    if(item in dish[3]):
        print(dish[1])
price=float(input("Please enter budget"))
for dish in menu:
    if(dish[2]<price):
        print(dish[1])




