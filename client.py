import socket
import time

HEADER = 32
PORT = 5060
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sendheader(msg):
    message = msg.encode(FORMAT)
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    message += b' ' * (HEADER - len(message))
    # client.sendall(send_length)
    client.sendall(message)

def sendpackage(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.sendall(send_length)
    client.sendall(message)
    print(client.recv(2048).decode(FORMAT))

def sendbet(msg):
    sendheader('BET')
    sendpackage(str(msg))

def sendspin(msg):
    sendheader('SPIN')
    sendpackage(str(msg))

def senddisconnect():
    sendheader(DISCONNECT_MESSAGE)

sendbet(3)
raw_input()
sendspin(42)
raw_input()
senddisconnect() 

# send(str(dict))
# input()
# send("Hello Everyone!")
# send("Hello Tim!")
# send(DISCONNECT_MESSAGE)


# msg_length = conn.recv(HEADER).decode(FORMAT)
        # msg_length = int(msg_length)
            # msg = conn.recv(msg_length).decode(FORMAT)
            # print(msg[0])
            # dict = ast.literal_eval(msg)
            # print(dict['Jantorno'])
            # print(dict['Bernardo'])