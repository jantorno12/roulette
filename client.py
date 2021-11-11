import pygame
from tkinter import *
import sys
from easygui import *
import socket
import ast
import os

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
    message += b' ' * (HEADER - len(message))
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

def rec_ans():
    msg = trata_msg()
    dict = ast.literal_eval(msg)
    return dict

def senddisconnect():
    sendheader(DISCONNECT_MESSAGE)

def sendbet(msg10, saldo):
    if(msg10 is None): # foi apertado o botao de cancelar
        return -1
    
    sendheader('BET')
    dict = sendpackage(str(msg10))
    print(dict)
    if (dict['resposta'] == 'Aposta invalida'):
        # tela de aposta invalida
        msgbox(msg = "Aposta invalida, aposte novamente",title = "Roleta")
        msg2 = integerbox(msg = 'Insira o valor da aposta\nSeu saldo é: ' + str(saldo), title='Roulette 1.0', lowerbound = 0, upperbound = saldo)
        return sendbet(msg2, saldo)
    else:
        gameLoop = True
        pygame.init()
        verde = [32, 82, 42]
        display = pygame.display.set_mode([840,480])
        pygame.display.set_caption("Jogo da Roleta")
        while gameLoop:
            for event in pygame.event.get():

                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] > 50 and mouse[0] < 150 and mouse[1] > 90 and mouse[1] < 150:
                        print("Escolha foi Par")
                        msg3 = 37
                        gameLoop = False
                        break
                    if mouse[0] > 50 and mouse[0] < 150 and mouse[1] > 160 and mouse[1] < 220:
                        print("Escolha foi Impar")
                        msg3 = 38
                        gameLoop = False
                        break
                    if mouse[0] > 50 and mouse[0] < 150 and mouse[1] > 230 and mouse[1] < 290:
                        print("Escolha foi  Vermelho")
                        msg3 = 39
                        gameLoop = False
                        break
                    if mouse[0] > 50 and mouse[0] < 150 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Preto")
                        msg3 = 40
                        gameLoop = False
                        break
                    if mouse[0] > 160 and mouse[0] < 260 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Primeira coluna")
                        msg3 = 41
                        gameLoop = False
                        break
                    if mouse[0] > 270 and mouse[0] < 370 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Segunda coluna")
                        msg3 = 42
                        gameLoop = False
                        break
                    if mouse[0] > 380 and mouse[0] < 480 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Terceira coluna")
                        msg3 = 43
                        gameLoop = False
                        break
                    if mouse[0] > 490 and mouse[0] < 600 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Primeira metade")
                        msg3 = 44
                        gameLoop = False
                        break
                    if mouse[0] > 610 and mouse[0] < 710 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Segunda metade")
                        msg3 = 45
                        gameLoop = False
                        break
                    if mouse[0] > 710 and mouse[0] < 810 and mouse[1] > 300 and mouse[1] < 360:
                        print("Escolha foi Primeira duzia")
                        msg3 = 46
                        gameLoop = False
                        break
                    if mouse[0] > 710 and mouse[0] < 810 and mouse[1] > 230 and mouse[1] < 290:
                        print("Escolha foi Segunda duzia")
                        msg3 = 47
                        gameLoop = False
                        break
                    if mouse[0] > 710 and mouse[0] < 810 and mouse[1] > 160 and mouse[1] < 220:
                        print("Escolha foi Terceira duzia")
                        msg3 = 48
                        gameLoop = False
                        break
                    if mouse[0] > 710 and mouse[0] < 810 and mouse[1] > 90 and mouse[1] < 150:
                        print("Escolha foi um Numero")
                        msg3 = integerbox(msg = 'Insira um numero entre 1 e 36 em que você quer apostar', title='Roulette 1.0', lowerbound = 1, upperbound = 36)
                        print(msg3)
                        gameLoop = False
                        break
                    if mouse[0] > 710 and mouse[0] < 810 and mouse[1] > 20 and mouse[1] < 80:
                        return -1
        

            #Draw
            display.fill([0, 0, 0])
            apostar = pygame.Rect(50,20,100,60)
            par = pygame.Rect(50,90,100,60)
            impar = pygame.Rect(50,160,100,60)
            vermelho = pygame.Rect(50, 230, 100, 60)
            preto = pygame.Rect(50, 300, 100, 60)
            primeiracoluna = pygame.Rect(160,300,100,60)
            segundacoluna = pygame.Rect(270, 300, 100, 60)
            terceiracoluna = pygame.Rect(380, 300, 100, 60)
            primeirametade = pygame.Rect(490, 300, 100, 60)
            segundametade = pygame.Rect(600, 300, 100, 60)
            primeiraduzia = pygame.Rect(710, 300, 100, 60)
            segundaduzia = pygame.Rect(710, 230, 100, 60)
            terceiraduzia = pygame.Rect(710, 160, 100, 60)
            numero = pygame.Rect(710, 90, 100, 60)
            sair = pygame.Rect(710, 20, 100, 60)
            pygame.draw.ellipse(display,[242,10,14], apostar)
            pygame.draw.rect(display, verde, par)
            pygame.draw.rect(display, verde, impar)
            pygame.draw.rect(display, verde, preto)
            pygame.draw.rect(display, verde, vermelho)
            pygame.draw.rect(display, verde, primeiracoluna)
            pygame.draw.rect(display, verde, segundacoluna)
            pygame.draw.rect(display, verde, terceiracoluna)
            pygame.draw.rect(display, verde, primeirametade)
            pygame.draw.rect(display, verde, segundametade)
            pygame.draw.rect(display, verde, primeiraduzia)
            pygame.draw.rect(display, verde, segundaduzia)
            pygame.draw.rect(display, verde, terceiraduzia)
            pygame.draw.rect(display, verde, numero)
            pygame.draw.ellipse(display,[242,10,14] , sair)

            dirname = os.path.dirname(os.path.abspath(__file__))
            image = pygame.image.load(os.path.join(dirname, "roletaokkk.jpg"))
            display.blit(image, (160, 90))

            txt = 'Faça sua aposta'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 15)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (60, 45))

            txt = 'PAR'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (80, 110))

            txt = 'ÍMPAR'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (70, 175))

            txt = 'VERMELHO'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 25)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (52, 252))

            txt = 'PRETO'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (70, 320))

            txt = 'PRIMEIRA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (175, 315))

            txt = 'COLUNA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (180, 335))

            txt = 'SEGUNDA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (285, 315))

            txt = 'COLUNA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (290, 335))

            txt = 'TERCEIRA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (395, 315))

            txt = 'COLUNA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (400, 335))

            txt = '1-18'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (515, 320))

            txt = '19-36'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (625, 320))

            txt = '1-12'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (740, 320))

            txt = '13-24'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (735, 250))

            txt = '25-36'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 30)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (735, 180))

            txt = ' NÚMERO'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 25)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (720, 110))

            txt = 'SAÍDA'  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 25)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (735, 40))

            txt = 'Seu saldo é: ' + str(saldo)  ##### armazena o texto
            pygame.font.init()  ##### inicia font
            fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
            fontesys = pygame.font.SysFont(fonte, 20)  ##### usa a fonte padrão
            txttela = fontesys.render(txt, 1, (250, 250, 250))  ##### renderiza o texto na cor desejada
            display.blit(txttela, (320, 40))


            pygame.display.update()
        pygame.display.quit()
        return sendspin(msg3)

def sendspin(msg):
    sendheader('SPIN')
    dict = sendpackage(str(msg))
    if (dict['resultado'] == 'Perdeu'):
        #tela mostrando perda
        msgbox(msg = "Você perdeu!",title = "Roleta")
        print('Perdeu a aposta')
    else:
        #tela mostrando vitoria
        msgbox(msg = "Você venceu!",title = "Roleta")
        print('Ganhou a aposta')
    print(dict)
    return dict['cliente']
<<<<<<< HEAD
=======
        
def senddisconnect():
    sendheader(DISCONNECT_MESSAGE)

m2 = 1
m3 = 1
while (m2 != '0' and m3 != 0):
    print('Defina o valor da aposta:')
    m1 = input()
    m3 = sendbet(int(m1))
    print('Se deseja parar, digite 0')
    m2 = input()
senddisconnect()
>>>>>>> 3d97dc22626a0d0f6ab9ef04b7371067746c6364

if __name__ == "__main__":
    saldo = 1000
    while (saldo != 0):
        msg2 = integerbox(msg = 'Insira o valor da aposta\nSeu saldo é: ' + str(saldo), title='Roulette 1.0', lowerbound = 0, upperbound = saldo)
        if(msg2 is None):
            break
        saldo = sendbet(msg2, saldo)
        if(saldo == -1):
            break
    senddisconnect()
    sys.exit()
