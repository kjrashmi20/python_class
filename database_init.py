import mysql.connector

def createDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE userdb")

def createTable():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="python12",
        database="userdb"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, phone_no VARCHAR(255), pwd VARCHAR(255), data VARCHAR(255))")

#createDB()
createTable()