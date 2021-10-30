import socket 
import ast
import random

HEADER = 32
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
min_bet = 5
saldo = {'cliente' : 1000, 'servidor': 1000}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def type_bet(tipo):
    resp = random.randint(-1, 36)
    if(tipo < 37):
        print(f'Foi apostado no numero {tipo}')
    if(tipo == 37):
        print(f'Foi apostado nos numeros pares')
    if(tipo == 38):
        print(f'Foi apostado nos numeros impares') 
    if(tipo == 39):
        print(f'Foi apostado nos numeros vermelhos') 
    if(tipo == 40):
        print(f'Foi apostado nos numeros pretos') 
    if(tipo == 41):
        print(f'Foi apostado na primeira coluna de numeros') 
    if(tipo == 42):
        print(f'Foi apostado na segunda coluna de numeros') 
    if(tipo == 43):
        print(f'Foi apostado na terceira coluna de numeros') 
    if(tipo == 44):
        print(f'Foi apostado nos numeros de 1 a 18') 
    if(tipo == 45):
        print(f'Foi apostado nos numeros de 19 a 36')
    if(tipo == 46):
        print(f'Foi apostado nos numeros de 1 a 12')
    if(tipo == 47):
        print(f'Foi apostado nos numeros de 13 a 24')
    if(tipo == 48):
        print(f'Foi apostado nos numeros de 25 a 36')
        
def check_bet(dict, bet):
    print(f'Valor enviado para aposta: {int(bet)}')
    # checando o valor da aposta
    if(bet < min_bet):
        return dict, 'Aposta invalida'
    else:
        ult_saldo = dict['cliente']
        dict['cliente'] = ult_saldo - bet
        return dict, 'Aposta valida'


def excludespace(strx):
    str_aux = ''
    for i in range(len(strx)):
        if(strx[i] != ' '):
            str_aux = str_aux + strx[i]
    return str_aux

def trata_msg(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length = int(excludespace(msg_length))
    msg = conn.recv(msg_length).decode(FORMAT)
    return msg

def sendpackage(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.sendall(send_length)
    client.sendall(message)
    print(client.recv(2048).decode(FORMAT))

def play_roulette(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        action_type = conn.recv(HEADER).decode(FORMAT)
        print(f'Tipo de comando: {action_type}')
        if action_type:
            if excludespace(action_type) == 'BET':
                msg = trata_msg(conn)
                saldo, ans = check_bet(int(msg))
                aux_dict = saldo
                aux_dict['resposta'] = ans

            if excludespace(action_type) == 'SPIN':
                msg = trata_msg(conn)
                saldo = type_bet(saldo, int(msg))
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
    print("Partida encerrada")
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    #Botar multi tread se quiser
    conn, addr = server.accept()
    play_roulette(conn,addr)


print("[STARTING] server is starting...")
start()