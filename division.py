#input two numbers, print if a is divisible by b

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=num1%num2
if (num3==0):
    print("{} is divisible by {}".format(num1,num2))
else:
    print("{} is not divisible by {}".format(num1,num2))





