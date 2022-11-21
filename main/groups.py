import sqlite3


def create_grp_table(grpname,path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS ?(members TEXT PRIMARY KEY,admin INT)'''
    cur.execute(query,(grpname,))
    connection.commit()
    cur.close()
    connection.close()

def view_all_members(grpname,path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f"SELECT members from {grpname}")
    user_info = cur.fetchall()
    for i in user_info:
        print(f"{i[0]}")
    cur.close()
    connection.close()

def insert_to_grp_db(path,grpname,username,isadmin):
    try:
        connection = sqlite3.connect(path)
        cur = connection.cursor()
        if isadmin:
            query = '''INSERT INTO ? VALUES(?,?)'''
            cur.execute(query,(grpname,username,1))
            print(f"Successfully created user {username}")
            return True
        else:
            query = '''INSERT INTO ? VALUES(?,?)'''
            cur.execute(query,(grpname,username,0))
            print(f"Successfully created user {username}")
            return True
    except:
        print(f"Failed to create user {username}")
        return False

def check_admin(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    try:
        cur.execute(f"SELECT admin from {grpname} WHERE username = {username}")
    except:
        print("Error checking admin")
    a = cur.fetchall()
    if a[0][0] == 1:
        return True
    else:
        return False

def make_admin(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    try:
        cur.execute(f"UPDATE {grpname} SET admin = 1 WHERE username ={username}")
    except:
        print("Error making admin")
    cur.close()
    connection.close()

def delete_member(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f"DELETE from {grpname} WHERE username ={username}")
    cur.close()
    connection.close()



    