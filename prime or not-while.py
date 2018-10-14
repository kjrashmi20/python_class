n=int(input("Enter number "))
prime=1
i=2
while(True):
    if(n%i==0):
        prime=0
        break;
    if(i==n-1):
        break;
    i=i+1
if(prime==1):
    print("This is a prime number")
else:
    print("This is not a prime number")
