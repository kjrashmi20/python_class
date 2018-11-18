list=[]
n=int(input("Please enter how many teams :"))
for i in range (1,n+1):
    team=input("PLease enter team name :")
    list.append(team)
list1=sorted(list)
print("The teams in sorted order are: {}".format(list1))



