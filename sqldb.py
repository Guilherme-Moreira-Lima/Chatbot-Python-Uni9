import mysql.connector
import user

mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)
dbcursor = mydb.cursor()


def create_user(username, userid):
    dbcursor.execute("INSERT INTO Client (`User_ID`, `UserName`, `UserPoints`) VALUES (%s, %s, 0);", (userid, username))
    mydb.commit()
    if dbcursor.rowcount > 0:
        return True
    else:
        return False

def delete_user(userid):
    dbcursor.execute("DELETE FROM Client WHERE User_ID = %s;", (userid,))
    mydb.commit()
    if dbcursor.rowcount > 0:
        return True
    else:
        return False

def get_user_points(userid):
    dbcursor.execute("SELECT UserPoints FROM Client WHERE User_ID = %s;", (userid,))
    return dbcursor.fetchall()

def verify_user(username, userid):
    dbcursor.execute("SELECT * FROM Client WHERE UserName = %s AND User_ID = %s;", (username,userid))
    return dbcursor.fetchall()

def add_points(userid):
    dbcursor.execute("UPDATE Client SET UserPoints = %s WHERE User_ID = %s;", (user.user_points, userid))
    mydb.commit()
    if dbcursor.rowcount > 0:
        return True
    else:
        return False

