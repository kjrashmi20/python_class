def multiplyTwoNumbers(a,b):#function name with multiplenames,use first letter caps,its a convention
    res=a*b
    return res

def factorial(n):
    res=1
    for i in range(2,n+1):
        res=res*i
    return res

res=factorial(5)
print(res)


