import socket, os, sys
from threading import Thread
import json

HOST, PORT = '127.0.0.1', 1234
NAME = input("Ingresar Nombre: ")

print("#"+"-"*30+"#")  #separator

BUFSIZE = 1024

ADDR = (HOST, PORT)

RESET = "\033[0;0m"
BOLD  = "\033[;1m"

INIT_CONEX = {
"request": "INIT_CONEX",
"body": [NAME,ADDR]
}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

client_socket.send(bytes(json.dumps(INIT_CONEX), 'UTF-8'))

left = False

def rc(): #rc > recieve
	while True:
		try:
			msg = json.loads(client_socket.recv(BUFSIZE).decode('UTF-8'))
			print(msg)
		except:
			break


#sys.stdout.write(BOLD+"Welcome {}. Puedes empezar a enviar mensajes!".format(NAME)+RESET+"\n")

while True:
	x = Thread(target=rc)
	x.start()
	print("BIENVENIDO A GOLF CARD GAME \n")
	opcion = input("1.Iniciar juego \n2.Salir\n")
	if opcion == '1':
		INICIO_JUEGO =  {
		"request": "INICIO_JUEGO",
		}
		client_socket.send(bytes(json.dumps(INICIO_JUEGO), 'UTF-8'))
		#msg = sys.stdin.readline()
	if opcion == '2':
		END_CONEX = {
 		"request": "END_CONEX"
		}
		left = True
		client_socket.send(bytes(json.dumps(END_CONEX), 'UTF-8'))
		client_socket.close()
		sys.exit()
		break