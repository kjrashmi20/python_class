a=int(input("Enter a number"))
while(True):
    n = int(input("Enter any random number"))
    if(n%a==0):
        print("{} is divisible by {}".format(n,a))
        break;

