import sqlite3
import bcrypt

def change_status_online(username,path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    query = '''UPDATE USERS SET status = 'ONLINE' where username = ? '''
    cur.execute(query,(username,))
    connection.commit()
    cur.close()
    connection.close()

def change_status_offline(username,path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    query = '''UPDATE users SET status = 'OFFLINE' where username = ? '''
    cur.execute(query,(username,))
    connection.commit()
    cur.close()
    connection.close()

def view_all(path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute("SELECT username,status from users")
    user_info = cur.fetchall()
    for i in user_info:
        print(f"{i[0]} : {i[1]}")
    cur.close()
    connection.close()

def view_online(path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute("SELECT username from users where status= 'ONLINE'")
    user_info = cur.fetchall()
    for i in user_info:
        print(i[0][0])
    cur.close()
    connection.close()

def create_table(path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY,salt TEXT,password TEXT, status TEXT)'''
    cur.execute(query)
    connection.commit()
    cur.close()
    connection.close()

def insert_to_db(cur,username,salt, password, status):
    try:
        query = '''INSERT INTO users VALUES(?,?,?,?)'''
        cur.execute(query,(username,salt,password,status))
        print(f"Successfully created user {username}")
        return True
    except:
        print(f"Failed to create user {username}")
        return False

def check_username(username,path):
    #check if the username exist
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute("SELECT username from users")
    a = cur.fetchall()
    if username in a:
        return True
    else:
        return False
    
def store_new_info(username, salt,password, status,path):
    #return True if success register
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    if(check_username(username,path)):
        cur.close()
        connection.commit()
        connection.close()
        return False
    else:
        if insert_to_db(cur,username, salt,password,status):
            cur.close()
            connection.commit()
            connection.close()
            return True
        else:
            return False

def show_all_user_info(path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute("SELECT * from users")
    user_info = cur.fetchall()
    for i in user_info:
        print(i)
    cur.close()
    connection.close()

def check_login_info(username, password, path):
    connection = sqlite3.connect(path)
    cur = connection.cursor()
    cur.execute("select salt from users where username=?",(username,))
    a = cur.fetchall()
    if len(a) == 0:
        return False
    salt = a[0][0]
    hashed = bcrypt.hashpw(password, salt)
    a = cur.execute("select password from users where username=?",(username,))
    a = cur.fetchall()
    if len(a) == 0:
        return False
    passw = a[0][0]
    if passw == hashed:
        return True
    else:
        return False