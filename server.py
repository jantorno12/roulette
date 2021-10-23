import socket 
import ast

HEADER = 32
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def excludespace(strx):
    str_aux = ''
    for i in range(len(strx)):
        if(strx[i] != ' '):
            str_aux = str_aux + strx[i]
    return str_aux

def play_roulette(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        action_type = conn.recv(HEADER).decode(FORMAT)
        print(action_type)
        if action_type:

            if excludespace(action_type) == 'BET':
                msg_length = conn.recv(HEADER).decode(FORMAT)
                msg_length = int(excludespace(msg_length))
                msg = conn.recv(msg_length).decode(FORMAT)
                print(msg[0])
                print(len(msg))
            if excludespace(action_type) == 'SPIN':
                print("oi")
            # msg_length = conn.recv(HEADER).decode(FORMAT)
            # msg_length = int(msg_length)
            # msg = conn.recv(msg_length).decode(FORMAT)
            # print(msg[0])
            # dict = ast.literal_eval(msg)
            # print(dict['Jantorno'])
            # print(dict['Bernardo'])
            if excludespace(action_type) == DISCONNECT_MESSAGE:
                connected = False

            conn.sendall("Msg received".encode(FORMAT))
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #Botar multi tread se quiser
    conn, addr = server.accept()
    play_roulette(conn,addr)


print("[STARTING] server is starting...")
start()