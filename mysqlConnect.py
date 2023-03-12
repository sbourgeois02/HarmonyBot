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
    print(usersInDB)

    #pseudologic
    #if user exists in database drop from userList
    #once all existing users are dropped from userList they will be added to the db

    insertSQL = 'Insert into user(UserName, UserTag, UserStatusID, UserRoleID) values (%s, %s, %s, %s);'
    
    values = []
    while len(userList) > 0:
        values.append((userList[0].name, userList[0].discriminator, 0, 0))
        userList.pop(0)

    print(values)

    cursor.executemany(insertSQL, values)

    print(cursor.rowcount, "record was inserted.")

    # Commit your changes in the database
    connection.commit()
    #close database
    connection.close()

        