import sqlite3


def create_grp_table(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    try:
        query = '''CREATE TABLE '''+ grpname +'''(usernames TEXT PRIMARY KEY,admin INT)'''
        cur.execute(query)
        print(f"Successfully created group {grpname}")
        query = '''INSERT INTO '''+grpname+''' VALUES(?,?)'''
        cur.execute(query,(username,1))
        connection.commit()
        cur.close()
        connection.close()
        return True
    except:
        return False

def view_all_members(path,grpname):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f"SELECT usernames from {grpname}")
    user_info = cur.fetchall()
    for i in user_info:
        print(f"{i[0]}")
    cur.close()
    connection.close()

def drop_table(path,grpname):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f"DROP TABLE {grpname}")
    cur.close()
    connection.close()

def add_member(path,grpname,username):
    try:
        connection = sqlite3.connect(path)
        cur = connection.cursor()
        query = '''INSERT INTO '''+grpname+''' VALUES(?,?)'''
        cur.execute(query,(username,0))
        print(f"Successfully added user {username} to the group {grpname}")
        return True
    except:
        print(f"Failed to add user {username} to the group {grpname}")
        return False

def check_admin(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    try:
        cur.execute(f"SELECT admin from {grpname} WHERE usernames = {username}")
    except Exception as e:
        print(e)
        # print("Error checking admin")
    a = cur.fetchall()
    print(a)
    if len(a) == 0:
        return False

    if a[0] == 1:
        return True
    else:
        return False

def make_admin(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    try:
        cur.execute(f"UPDATE {grpname} SET admin = 1 WHERE usernames = {username}")
    except:
        print("Error making admin")
    cur.close()
    connection.close()

def delete_member(path,grpname,username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f"DELETE from {grpname} WHERE usernames ={username}")
    cur.close()
    connection.close()

## TODO
## Make this function work
## I hab made new function, hopefully it works XD
def view_all_groups(path, username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute(f"select m.name from pragma_table_info m")
    cur.close()
    connection.close()

def in_grp(path, grpname, username):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    result = cur.execute(f"SELECT * FROM {grpname} WHERE usernames = {username}").fetchall()
    cur.close()
    connection.close()
    if len(result) == 0:
        return False
    else:
        return True