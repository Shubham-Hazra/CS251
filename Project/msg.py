class msg:
    def __init__(self,type,sender,reciever,msg):
        self.type = type
        self.sender = sender
        self.reciever = reciever
        self.length = len(msg)
        self.msg = msg

class group_msg:
    def __init__(self,type,sender,group_name,msg):
        self.type = type
        self.sender = sender
        self.reciever = group_name
        self.length = len(msg)
        self.msg = msg