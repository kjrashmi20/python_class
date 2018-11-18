def modifyInteger(a):
    a=100
def modifyFloat(f):
    f=2.5
def modifyString(s):
    s="Modify this"
def modifyList(l):
    l.append("Add new value")
def modifyDict(d):
    d[10]:"len"

a=10
print("Before funtion call:a={}".format(a))
modifyInteger(a)
print("After function call:a={}".format (a))
print("*"*60)
b=10.5
print("Before funtion call:b={}".format(b))
modifyFloat(b)
print("After function call:b={}".format (b))
print("*"*60)
s="Original"
print("Before funtion call:s={}".format(s))
modifyString(s)
print("After function call:s={}".format (s))
print("*"*60)
l=["First","Second"]
print("Before funtion call:l={}".format(l))
modifyList(l)
print("After function call:l={}".format (l))
print("*"*60)
d={1:"one",2:"Two"}
print("Before funtion call:d={}".format(d))
modifyDict(d)
print("After function call:d={}".format (d))


