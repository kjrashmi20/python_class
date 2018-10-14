#palindrome

a=input("enter word")
reve=a[-1::-1]
print(reve)
if(reve==a):
    print("{}is a palindrome".format(a))
else:
    print("{} is not a palindrome".format(a))
