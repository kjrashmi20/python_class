count=0
def counterFunc1():
    global count #takes value of variable as declared globally
    print("1:I got called")
    count=count+1
    print(count)
def counterFunc2():
    global count
    print("2:I got called")
    count=count+1
    print(count)
def counterFunc3():
    global count
    print("3:I got called")
    count=count+1
    print(count)

print("Before call count={}".format(count))
counterFunc1()
counterFunc1()
counterFunc1()
counterFunc1()
counterFunc1()

counterFunc2()
counterFunc2()
counterFunc2()

counterFunc3()
counterFunc3()
print("After call count={}".format(count))