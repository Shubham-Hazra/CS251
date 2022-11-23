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
group_info_db_path ="databases/groups.db"
messages_db_path = "databases/messages.db"

# signin stuff
if len(sys.argv)==3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
else:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

# other global variables and constants
BUFSIZE = 4194304
ADDR = (HOST, PORT)
AD = {}
# TODO
LOCAL = '127.0.0.1'
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
create_read_table(messages_db_path)
create_unread_table(messages_db_path)
###################

while True:
    try:
        data, addr = server_sock.recvfrom(BUFSIZE)
        # print(addr)
    except:
        print('a connection closed')
        break

    # to decode the data
    message = pickle.loads(data)
    msgtype = message.type
    sender = message.sender
    receiver = message.receiver
    msg_ = message.msg
    grp = message.group_name
    # print(sender,msg_,msgtype)
    if msgtype == 'connect':
        # if addr not in AD.values():
        # if not isPortinTable(user_info_db_path, addr[1]):
        # if check_status(user_info_db_path, sender) == "OFFLINE":
            # pub_keys[sender] = msg_
            # for name, address in AD.items():
            #     package = pickle.dumps(msg('key', sender, name,msg_))
            #     server_sock.sendto(package, address)
            # AD[sender] = addr
            # for name, pubkey in pub_keys.items():
            #     if name == sender:
            #         continue
            
            #     server_sock.sendto(package, addr)
            message = f"{sender} has entered the chat "
            # for name, address in AD.items():
            change_status_online(sender, user_info_db_path)
            # print(get_all_active_ports(user_info_db_path))
            for name, port in get_all_active_ports(user_info_db_path):
                if name != sender:
                    package = pickle.dumps(msg('receive', 'server', name,message))
                    server_sock.sendto(package, (LOCAL, port))
    elif msgtype == 'receive':
        # if(receiver in AD):
        print(check_username(receiver, user_info_db_path))
        if check_username(receiver, user_info_db_path):
            print(get_port(user_info_db_path, receiver))
            server_sock.sendto(data, ('localhost', get_port(user_info_db_path, receiver)))
        else:
            message = f"{receiver} does not exist"
            package = pickle.dumps(msg('recieve','server', sender,message))
            server_sock.sendto(package, addr)
    elif msgtype == 'group':
        if msg_ == "create":
            if create_grp_table(group_info_db_path, grp, sender):
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success_created_table', grp)), addr)
                addmem = pickle.loads(server_sock.recv(BUFSIZE))
                while addmem.msg != 'exit':
                    if add_member(group_info_db_path, addmem.group_name, addmem.receiver):
                        server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success', grp)), addr)
                        message = f"You have been added to the group {addmem.group_name}"
                        package = pickle.dumps(msg('receive', 'server', addmem.receiver,message))
                        # server_sock.sendto(package, AD[addmem.receiver])
                        server_sock.sendto(package, (LOCAL, get_port(user_info_db_path, addmem.receiver)))
                    addmem = pickle.loads(server_sock.recv(BUFSIZE))
            else:
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'failed_create_table', grp)), addr)
        elif msg_ == "add":
            if check_admin(group_info_db_path, grp, sender):
                server_sock.sendto(pickle.dumps(msg('group', sender, sender, 'added_successfully', grp)), addr)
                stuff = server_sock.recv(BUFSIZE)
                addmem = pickle.loads(stuff)
                if add_member(group_info_db_path, addmem.group_name, addmem.receiver):
                    server_sock.sendto(pickle.dumps(msg('group', addmem.receiver, sender, 'success', grp)), addr)
                    server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success', grp)), addr)
                    message = f"You have been added to the group {addmem.group_name}"
                    package = pickle.dumps(msg('receive', 'server', addmem.receiver,message))
                    # server_sock.sendto(package, AD[addmem.receiver])
                    server_sock.sendto(package, (LOCAL, get_port(user_info_db_path, addmem.receiver)))
                else:
                    server_sock.sendto(pickle.dumps(msg('group', addmem.receiver, sender, 'failed_adding', grp)), addr)
            else:
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'not_admin', grp)), addr)     
        elif msg_ == "delete":
            if check_admin(group_info_db_path, grp, sender):
                drop_table(group_info_db_path, grp)
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'group_deleted', grp)), addr)
            else:
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'failed_deleting_group', grp)), addr)

        elif msg_ == "kick":
            if check_admin(group_info_db_path, grp, sender):
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'kicked_successfully', grp)), addr)
                stuff = server_sock.recv(BUFSIZE)
                delmem = pickle.loads(stuff)
                if delete_member(group_info_db_path, grp, delmem.receiver):
                    server_sock.sendto(pickle.dumps(msg('group', delmem.receiver, sender, 'success', grp)), addr)
                    server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'success', grp)), addr)
                    message = f"You have been kicked from the group {delmem.group_name} by {delmem.sender}"
                    package = pickle.dumps(msg('receive', 'server', delmem.receiver,message))
                    # server_sock.sendto(package, AD[delmem.receiver])
                    server_sock.sendto(package, (LOCAL, get_port(user_info_db_path, delmem.receiver)))
                else:
                    server_sock.sendto(pickle.dumps(msg('group', delmem.receiver, sender, 'failed_kicking', grp)), addr)
            else:
                server_sock.sendto(pickle.dumps(msg('group', 'server', sender, 'not_admin', grp)), addr)
        else:
            # if(receiver in AD):
            # print("reached here")
            if check_username(receiver, user_info_db_path):
                # print("didn't reach here")
                # server_sock.sendto(data, AD[receiver])
                server_sock.sendto(data, (LOCAL, get_port(user_info_db_path, receiver)))
            else:
                message = f"{receiver} does not exist"
                package = pickle.dumps(msg('recieve','server', sender,message))
                server_sock.sendto(package, addr)
            ## MOST PROBABLY UNNECESSARY PIECE OF CODE
            #send_to()
        # else:
        #     message = f"{receiver} does not exist"
        #     package = pickle.dumps(msg('recieve','server', sender,message))
        #     server_sock.sendto(package, addr)
    elif msgtype == 'disconnect':
        # if(sender in AD):
        if check_username_online(user_info_db_path, sender):
            # AD.pop(sender)
            # pub_keys.pop(sender)
            # for name, addr in AD.items():
            for name, port in get_all_active_ports(user_info_db_path):
                package = pickle.dumps(msg('disconnect', sender, name,'cancel'))
                server_sock.sendto(package, (LOCAL, port))
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
        pubkey = server_sock.recv(BUFSIZE)
        privkey = server_sock.recv(BUFSIZE)
        # print(port, sender)
        state = store_new_info(user_info_db_path, username, salt,hashed,'ONLINE', addr[1], pubkey, privkey)
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
            update_port(user_info_db_path, sender, addr[1])
            server_sock.sendto(package, addr)
        else:
            package = pickle.dumps(msg('login', 'server', 'unknown', 'fail'))
            server_sock.sendto(package, addr)
    else:
        # if(receiver in AD):
        if check_username(receiver, user_info_db_path):
            # server_sock.sendto(data, AD[receiver])
            server_sock.sendto(data, (LOCAL, get_port(user_info_db_path, receiver)))
        else:
            server_sock.sendto(message, addr)


server_sock.close()