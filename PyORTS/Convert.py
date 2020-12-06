import socket
import serial
import threading
while True:
    port = input("Escriba el puerto serial donde tienes conectado tu arduino o microcontrolador: ")
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(('localhost', 5090))
    except:
        print("El servidor esta cerrado, compruebe que este conectado e intentelo de nuevo")
    try:
        s = serial.Serial(port, 115200, timeout=0.05)
        if s.isOpen():
            break;
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
hilo1 = threading.Thread(target=SerialToTCP)
hilo2 = threading.Thread(target=TCPToSerial)
hilo1.start()
hilo2.start()



