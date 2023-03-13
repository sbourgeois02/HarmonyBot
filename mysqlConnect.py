#pip install mysqlclient
#docs https://mysqlclient.readthedocs.io/
import os

import MySQLdb
from dotenv import load_dotenv

#load the environment variables
load_dotenv()

def main():
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))

    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')

    cursor.execute('SELECT name FROM language WHERE language_id = 1')
    results = cursor.fetchone()

    print(results)

#onload the bot will check the database and load into it unadded things
def onLoad(userList, roleList):
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
    if len(addUserList) is 1:
        addUserList.pop(0)

    print(addUserList)

    # #check if roles are in database
    # cursor.execute('Select RoleID from role')
    # rolesInDB = cursor.fetchall()

    # print("Stored Roles: ", rolesInDB)
    # print(rolesInDB[0][0:1])
    # for role in roleList:
    #     print(str(role[0])[0:6])

    # for role in roleList:
    #     for currDBRole in rolesInDB:
    #         if str(role[0])[0:6] is currDBRole[1:7]:
    #             roleList.pop(0)

    # print(roleList)

    #add roles
    insertRolesSQL = 'Insert into role(RoleID, RoleName) values (%s, %s)'

    roleValues = []
    #print(roleList)
    for role in roleList:
        #print(role)
        roleValues.append((str(role[0])[0:6], role[1]))
        roleList.pop(0)

    #print(roleValues)

    cursor.executemany(insertRolesSQL, roleValues)

    print(cursor.rowcount, "record was inserted.")

    #once addUserList is finalized it is added to the DB

    insertUsersSQL = 'Insert into user(UserName, UserTag, UserStatusID, UserRoleID) values (%s, %s, %s, %s);'
    
    userValues = []
    while len(addUserList) > 0:
        userValues.append((addUserList[0][0], addUserList[0][1], addUserList[0][2], str(1062091327392731247)[0:6]))
        addUserList.pop(0)

    #print(userValues)

    cursor.executemany(insertUsersSQL, userValues)

    print(cursor.rowcount, "record was inserted.")

    



    # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

def storeCommands(name, perm, script):
    connection = MySQLdb.connect(host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),passwd=os.getenv('DB_PASSWORD'),db=os.getenv('DB_SCHEMA'))

    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()

    if db:
        print("You're connected to database: ", db)
    else:
        print('Not connected.')


    sqlInput = "Insert into commands(CommandInput, CommandAction, CommandMinRoleID) values(%s, %s, %s)"
    commandValues = [name, script, perm]

    cursor.execute(sqlInput, commandValues)

    # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()