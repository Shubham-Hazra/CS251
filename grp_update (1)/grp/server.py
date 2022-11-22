import socket
from user_info import *
from groups import *
from time import ctime, sleep
import sys
import pickle
from msg import *
from colorama import init
from termcolor import colored
from messages import *
import bcrypt

# initializing database path, not required with postgresql
user_info_db_path = "databases/userInfo.db"

# signin stuff
if len(sys.argv)==3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
else:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

# other global variables and constants
BUFSIZE = 4096
ADDR = (HOST, PORT)
AD = {}
# TODO

pub_keys = {}
groups = {}

# binding server socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(ADDR)

print(f"Listening on {(HOST,PORT)}")
# TODO
# will have to be changed, if multiple servers are being implemented
###################
create_table(user_info_db_path)
###################

while True:
    try:
        data, addr = server_sock.recvfrom(BUFSIZE)
    except:
        print('a connection closed')
        break

    # to decode the data
    message = pickle.loads(data)
    msgtype = message.type
    sender = message.sender
    receiver = message.receiver
    length = message.length
    msg_ = message.msg
    grp = message.group_name
    if msgtype == 'connect':
        if addr not in AD.values():
            pub_keys[sender] = msg_
            for name, address in AD.items():
                package = pickle.dumps(msg('key', sender, name,msg_))
                server_sock.sendto(package, address)
            AD[sender] = addr
            for name, pubkey in pub_keys.items():
                if name == sender:
                    continue
                package = pickle.dumps(msg('key', name, sender,pubkey))
                server_sock.sendto(package, addr)
            message = f"{sender} has entered the chat "
            for name, address in AD.items():
                if name != sender: 
                    package = pickle.dumps(msg('receive', 'server', name,message))
                    server_sock.sendto(package, address)
    elif msgtype == 'receive':
        if(receiver in AD):
            server_sock.sendto(data, AD[receiver])
        else:
            message = f"{receiver} does not exist"
            package = pickle.dumps(msg('recieve','server', sender,message))
            server_sock.sendto(package, addr)
    elif msgtype == 'group':
        print(msg_)
        if msg_ == "create":
            if create_grp_table(user_info_db_path, grp, sender):
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success_created_table', grp)), addr)
                print("SENT")
                addmem = pickle.loads(server_sock.recv(BUFSIZE))
                while addmem.msg != 'exit':
                    if add_member(user_info_db_path, addmem.group_name, addmem.receiver):
                        server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success', grp)), addr)
                    addmem = pickle.loads(server_sock.recv(BUFSIZE))
            else:
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'failed_create_table', grp)), addr)
                print("SENT")
        elif msg_ == "add":
            if check_admin(user_info_db_path, grp, sender):
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'admin', grp)), addr)
                stuff = server_sock.recv(BUFSIZE)
                addmem = pickle.loads(stuff)
                if add_member(user_info_db_path, addmem.group_name, addmem.receiver):
                    server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success', grp)), addr)
            else:
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'fail', grp)), addr)
            
        elif msg_ == "delgrp":
            pass
        elif msg_ == "kick":
            pass
        else:
            pass
            #send_to()
        # else:
        #     message = f"{receiver} does not exist"
        #     package = pickle.dumps(msg('recieve','server', sender,message))
        #     server_sock.sendto(package, addr)
    elif msgtype == 'disconnect':
        if(sender in AD):
            AD.pop(sender)
            pub_keys.pop(sender)
            for name, addr in AD.items():
                package = pickle.dumps(msg('disconnect', sender, name,'cancel'))
                server_sock.sendto(package, addr)
            change_status_offline(sender,user_info_db_path)
        else:
            message = f"{receiver} does not exist"
            package = pickle.dumps(msg('recieve','server', sender,message))
            server_sock.sendto(package, addr)
    elif msgtype == 'register':
        username, password = (msg_).split(' ', 1)
        password = password.encode()
        # Adding the salt to password
        salt = bcrypt.gensalt()
        # Hashing the password
        hashed = bcrypt.hashpw(password, salt)  
        state = store_new_info(username, salt,hashed,'ONLINE', user_info_db_path)
        if(state):
            package = pickle.dumps(msg('register', 'server', 'unknown','success'))
            server_sock.sendto(package, addr)
        else:
            package = pickle.dumps(msg('register', 'server', 'unknown','fail'))
            server_sock.sendto(package, addr)
    elif msgtype == 'login':
        username, password = (msg_).split(' ', 1) 
        password = password.encode() 
        state = check_login_info(username, password, user_info_db_path)
        if(state):
            package = pickle.dumps(msg('login', 'server', 'unknown','success'))
            change_status_online(sender, user_info_db_path)
            server_sock.sendto(package, addr)
        else:
            package = pickle.dumps(msg('login', 'server', 'unknown', 'fail'))
            server_sock.sendto(package, addr)
server_sock.close()