import socket
import time
import ast

HEADER = 32
PORT = 5060
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def excludespace(strx):
    str_aux = ''
    for i in range(len(strx)):
        if(strx[i] != ' '):
            str_aux = str_aux + strx[i]
    return str_aux

def trata_msg():
    msg_length = client.recv(HEADER).decode(FORMAT)
    msg_length = int(excludespace(msg_length))
    msg = client.recv(msg_length).decode(FORMAT)
    return msg

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
    dict = rec_ans()
    return dict
    # print(client.recv(2048).decode(FORMAT))

def sendbet(msg):
    sendheader('BET')
    dict = sendpackage(str(msg))
    print(dict)
    if (dict['resposta'] == 'Aposta invalida'):
        print('Valor incompativel')
        print('Aposte outro valor')
        msg2 = input()
        return sendbet(msg2)
    else:
        print('Insira sua aposta')
        msg3 = input()
        return sendspin(msg3)

def rec_ans():
    msg = trata_msg()
    dict = ast.literal_eval(msg)
    return dict

def sendspin(msg):
    sendheader('SPIN')
    dict = sendpackage(str(msg))
    if (dict['resultado'] == 'Perdeu'):
        print('Perdeu a aposta')
    else:
        print('Ganhou a aposta')
    print(dict)
    return dict['cliente']
        
def senddisconnect():
    sendheader(DISCONNECT_MESSAGE)

m2 = 1
m3 = 1
while (m2 != '0' and m3 != 0):
    print('Defina o valor da aposta:')
    m1 = input()
    m3 = sendbet(m1)
    print('Se deseja parar, digite 0')
    m2 = input()
senddisconnect()

