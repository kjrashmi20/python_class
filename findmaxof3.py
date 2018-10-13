a=int(input("enter num1"))
b=int(input("enter num2"))
c=int(input("enter num3"))
if(a>b):
    if(c>a):
        print("Max is {}".format(c))
    else:
        print("Max is {}".format(a))
else:
    if(c>b):
        print("Max is {}".format(c))
    else:
        print("Max is {}".format(b))

