import mysql.connector

def insertDataInTable(data):

    mydb = mysql.connector.connect(host="localhost",
        user="root",
        passwd="python12",
        database="userdb"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO user (phone_no, pwd, data) VALUES (%s, %s, %s)"
    val = (data[0],data[1] ,data[2])
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def newUser():
    phoneno = input("Please enter your phone no :")
    password = input("Please enter your password:")
    blog = input("Whats the title of your blog:")
    #checkDuplicate()
    data = []
    data.append(phoneno)
    data.append(password)
    data.append(blog)
    insertDataInTable(data)

def readDataFromTable(phoneno):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12",
        database="userdb"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM user WHERE phone_no = {}".format(phoneno)
    #data = (phoneno,)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        return x
    return []

def existingUser():
    phoneno = input("Please tell your phone no:")
    password = input("Please tell your password")
    read_data = readDataFromTable(phoneno)
    print(type(read_data))
    print(read_data)
    if read_data[2] == password:
        print("Login successful ")
        print("Your blog is titled : {}".format(read_data[3]))
    else:
        print("Login unsuccessful . Wrong phone no or password !")

def mainLoop():
    while(True):
        print("Existing user(enter 1) or New User(Enter 2) ? -- (Enter 0 to exit)")
        res = int(input())
        if res == 1:
            existingUser()
        elif res == 2:
            newUser()
        else:
            break
    print("Thanks for visiting our website")

mainLoop()