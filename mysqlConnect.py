#pip install mysqlclient
#docs https://mysqlclient.readthedocs.io/
import os

import MySQLdb
from dotenv import load_dotenv

#load the environment variables
load_dotenv()

#onload the bot will check the database and load into it unadded things
def onLoad(userList):
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),
                                 user=os.getenv('DB_USER'),
                                 passwd=os.getenv('DB_PASSWORD'),
                                 db=os.getenv('DB_SCHEMA'))
    
    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')

    cursor.execute('Select UserName, UserTag from user')
    usersInDB = cursor.fetchall()

    addUserList =[]
    print(userList)

    while len(userList) > 0:
        if userList[0].bot is True:
            userList.pop(0)
            continue
        if len(userList[0].roles) > 1:
            roleID = convertRoleID(userList[0].roles[1])
            print(roleID)
            addUserList.append((userList[0].name, userList[0].discriminator, 0, roleID))
        else:
            addUserList.append((userList[0].name, userList[0].discriminator, 0, 0))
        userList.pop(0)

    print("Add User List: \n")
    print(addUserList, "\n")

    #if user exists in database drop from userList
    for currDBUser in usersInDB:
        print("Users remaining: \n")
        for currUser in addUserList:
            print(currUser[0], currUser[1])

        print("\n")
        
        for currUser in addUserList:
            print(currDBUser[0], currDBUser[1])
            print(currUser[0], currUser[1])
            if currUser[0] == currDBUser[0] and currUser[1] == currDBUser[1]:
                print("\n User Dropped: ", currUser[0], currUser[1], "\n")
                addUserList.pop(0)
                break;

    print(addUserList)

    #hardcode bug fix
    if len(addUserList) == 1:
        addUserList.pop(0)

    print(addUserList)


    

    #once addUserList is finalized it is added to the DB

    insertUsersSQL = 'Insert into user(UserName, UserTag, UserStatusID, UserRoleID) values (%s, %s, %s, %s);'
    
    userValues = []
    while len(addUserList) > 0:
        userValues.append((addUserList[0][0], addUserList[0][1], addUserList[0][2], addUserList[0][3]))
        addUserList.pop(0)

    #print(userValues)

    cursor.executemany(insertUsersSQL, userValues)

    print(cursor.rowcount, "record was inserted.")

    



    # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

def storeCommands(name, output):
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))

    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')


    sqlInput = "Insert into commands(CommandInput, CommandAction) values(%s, %s)"
    commandValues = [name, output]

    cursor.execute(sqlInput, commandValues)

    # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

def customExecute(commandName):
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))

    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')


    sqlInput = "select commandAction from commands where commandInput = %s"
    commandValues = [commandName]
    print(commandName)

    cursor.execute(sqlInput, commandValues)
    results = cursor.fetchone()

    print(str(results))
    # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

    results = str(results)

    results = results[2:len(results)-3]

    print(results)

    return str(results)

def pullProfanity():
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))
    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')

    cursor.execute("select badwords from Modwords")
    badWords = cursor.fetchall()

    print(badWords)

     # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

    return badWords

def pullStrikes():
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))
    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')

    cursor.execute("select UserName, UserTag, UserNumStrikes from user")
    userStrikes = cursor.fetchall()

    print(userStrikes)

     # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

    return userStrikes

def updateStrikes(name, tag, numStrikes):
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))
    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')

    sqlInput = "update user set UserNumStrikes = %s where UserName = %s amd UserTag = %s"
    commandValues = [numStrikes, name, tag]
    cursor.execute(sqlInput, commandValues)

     # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()


def convertRoleID(roles):

    print(roles.id)
    
    dbID = 0
    
    if roles.id == "Administrator":
        dbID = 4
    elif roles.id == "Power Moderator":
        dbID = 3
    elif roles.name == "Moderator": # == os.getenv('MOD_ROLE_ID'):
        dbID = 2
    elif roles.id == "SuperUser":
        dbID = 1
    

    print(dbID)

    return dbID