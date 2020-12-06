import socket
import serial
import threading

port = input("Escriba el puerto serial donde tienes conectado tu arduino o microcontrolador: ")
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 5090))
try:
  s = serial.Serial(port, 115200, timeout=0.05)
except:
  print("El Puerto ya esta ocupado, intente otro")

def SerialToTCP():
    while True:
        data = s.read(128)
        c.sendall(data)
def TCPToSerial():
    while True:
        data = c.recv(128)
        s.write(data)

hilo1 = threading.Thread(target=SerialToTCP)
hilo2 = threading.Thread(target=TCPToSerial)
hilo1.start()
hilo2.start()
