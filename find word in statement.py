stat1=input("statement1")
stat2=input("statement2")
word=input("enter word")
if(word in stat1):
    if (word in stat1 and word in stat2):
        print("word in both statement")
    else:
        print("word is in statement1")
elif(word in stat2):
    print("word in statement2")
else:
    print("word not in any statement")

