import socket
import serial
import threading

port = input("Escribe el puerto serial donde tienes conectado tu arduino: ")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 5090))
s = serial.Serial(port, 115200, timeout=0.05)
#c.send("register(asfa::pulsador::ilum::*)\nregister(asfa::leds::*)\nregister(asfa::pantalla::iniciar)\nregister(asfa::pantalla::apagar)\nregister(asfa::sonido::iniciar)\nregister(asfa::sonido::detener)\n".encode())

def SerialToTCP():
    while True:
        data = s.read(128)
        c.sendall(data)
def TCPToSerial():
    while True:
        data = c.recv(128,)
        s.write(data)

hilo1 = threading.Thread(target=SerialToTCP)
hilo2 = threading.Thread(target=TCPToSerial)
hilo1.start()
hilo2.start()

