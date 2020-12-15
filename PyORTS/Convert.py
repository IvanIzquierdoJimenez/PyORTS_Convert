import socket
import serial
import serial.tools.list_ports
import threading
import os

list = serial.tools.list_ports.comports()
connected = []
for element in list:
    connected.append(element.device)
print("Puertos disponibles: " + str(connected)[1:-1])

while True:
    port = input("Escriba el puerto serial donde tienes conectado tu arduino o microcontrolador: ")
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(('localhost', 5090))
        if c.isOpen():
            break;
        s = serial.Serial(port, 115200, timeout=0.05)
        if s.isOpen():
            break;
    except socket.error:
        print("El servidor esta cerrado, compruebe que este conectado e intentelo de nuevo")
    except:
        print("El Puerto ya esta ocupado o no existe, porfavor intente otro")

def SerialToTCP():
    while True:
        try:
            data = s.read(128)
            c.sendall(data)
        except:
            return
def TCPToSerial():
    while True:
        try:
            data = c.recv(128)
            s.write(data)
        except:
            return
StT = threading.Thread(target=SerialToTCP)
TtS = threading.Thread(target=TCPToSerial)
StT.start()
TtS.start()



