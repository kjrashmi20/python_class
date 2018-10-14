data=input("Enter a alphanumeric string")
res="8"
for c in data :
    if(c in "123456789"):
        res=res+c #concatenation
print(res)
