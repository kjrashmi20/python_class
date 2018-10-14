n=int(input("Enter range"))
x=int(input("Enter number to check divisibility"))
count=0
for i in range(1,n+1):
    if(i%x==0):
        count=count+1
        print(i)
print(count)