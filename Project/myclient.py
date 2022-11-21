from data import *
import sys
import socket
import rsa
from time import ctime
import getpass
import pickle
import threading
from msg import *

buffer = 4096
db_path = "databases/userInfo.db"
pub_keys={}

if len(sys.argv)==3:
    host = sys.argv[1]
    port = int(sys.argv[2])
else:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

addr = (host,port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try :
    s.connect((host, port))
except :
    print("\33[31m\33[1m Can't connect to the server \33[0m")
    sys.exit()

def show_message(sender, msg):
        if(sender != 'server'):
            pass
            # msg = rsa.decrypt(msg, priv)
        msg = msg+ ctime()
        if(sender != 'server'):
            msg = sender+": "+msg   
        print(msg)


def recv_message():
        while True:
            msg = s.recv(buffer)
            if not msg:
                sys.exit(0)
            if len(msg) != 0:
                message = pickle.loads(msg)
                if(message.type == 'recieve'):
                    show_message(message.sender,message.msg)
                elif(message.type == 'key'):
                    public_partner_key = message.msg
                    pub_keys[message.sender] = public_partner_key
                elif(message.type == 'group'):
                    pass
                elif(message.type == 'disconnect'):
                    pub_keys.pop(message.sender)

def send_message(username):
    while True:
        message = input("Enter: ")
        for r_name, key in pub_keys.items():
            package = pickle.dumps(msg('receive', username, r_name,message))
            s.sendto(package,addr)

def main():
    print(pub_keys)
    print("1 - LOGIN")
    print("2 - NEW USER")
    opt = int(input(">>> "))
    if(opt == 1):
        username = input("Username: ")
        password = getpass.getpass()
        message = username+" "+password
        data = pickle.dumps(msg('login',username,'server',message))
        s.sendto(data,addr)
        conf = s.recv(buffer)
        message = pickle.loads(conf).msg
        if message == 'success':
            print(f"Welcome back {username}")
        else:
            print("Invalid login")
            sys.exit(1)
    elif(opt == 2):
        while True:
            username = input("Username: ")
            password = getpass.getpass()
            message = username+" "+password
            data = pickle.dumps(msg('register',username,'server',message))
            s.sendto(data,addr)
            conf = s.recv(buffer)
            message = pickle.loads(conf).msg
            if message == 'success':
                print(f"You have successfully registered")
                break
            else:
                print("Username already taken. Try another username")
                continue
    public_key,private_key = rsa.newkeys(1024)
    message = public_key.save_pkcs1("PEM")
    data = pickle.dumps(msg('connect',username,'server',message))
    s.sendto(data,addr)
    recieve_thread = threading.Thread(target=recv_message)
    recieve_thread.start()
    # send_message(username)

    # while opt != 6:
    #     print("1 - VIEW ALL")
    #     print("2 - VIEW ONLINE")
    #     print("3 - VIEW GROUPS")
    #     print("4 - ENTER DIRECT MESSAGE")
    #     print("5 - ENTER GROUP")
    #     print("6 - Quit")
    #     opt = int(input(">>> "))
    #     if(opt == 1):
    #         view_all(db_path)
    #     elif(opt == 2):
    #         view_online(db_path)
    #     elif(opt == 3):
    #         pass
    #     elif(opt == 4):
    #         to_name = input("Whom do you want to chat to: ")
    #         msg=input(">>> ")
    #         s.send(username.encode('ascii'))
    #         while True:
    #             socket_list = [sys.stdin, s]
    #             # Get the list of sockets which are readable
    #             rList, wList, error_list = select.select(socket_list , [], [])
    #             for sock in rList:
    #                 #incoming message from server
    #                 if sock == s:
    #                     data = sock.recv(4096)
    #                     # print(data)
    #                     if not data :
    #                         print('\33[31m\33[1m \rDISCONNECTED!!\n \33[0m')
    #                         sys.exit()
    #                     else :
    #                         sys.stdout.write(data.decode('ascii'))
    #                 #user entered a message
    #                 else :
    #                     s.send(msg.encode('ascii'))
    #                     s.send(to_name.encode('ascii'))
    #     elif(opt == 5):
    #         group = input("Which group chat do you want to enter: ")
    #         if(group.capitalize().strip() == "ALL"):
    #             pass
    #     else:
    #         break
        
    
    # change_status_offline(username,db_path)


if __name__ == "__main__":
    main()