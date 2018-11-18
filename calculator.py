while True:
    print("1:Do you want to add two numbers ?")
    print("2:Do you want to subtract two numbers?")
    print("3:Do you want to multiply two numbers?")
    print("4:Do you want to divide two numbers?")
    print("5: Exit program")
    a=int(input("Select option"))
    if a==1:
        add=int(input("Enter first number"))
        add1=int(input("Enter second number"))
        result=add+add1
        print(result)
    elif a==2:
        sub=int(input("Enter first number"))
        sub1=int(input("Enter second number"))
        result=sub-sub1
        print(result)
    elif a==3:
        mul = int(input("Enter first number"))
        mul1 = int(input("Enter second number"))
        result = mul*mul1
        print(result)
    elif a==4:
        div = int(input("Enter first number"))
        div1 = int(input("Enter second number"))
        result = div/div1
        print(result)
    elif a==5:
        print("Exiting the program, Thank you!")
        break;








