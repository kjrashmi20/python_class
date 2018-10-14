n=int(input("Enter number "))
prime=1
for i in range(2,n):
    if(n%i==0):
        prime=0
        break;
if(prime==1):
    print("This is a prime number")
else:
    print("This is not a prime number")


