import serial
import time

port = 'COM4'
baund_rate = 115200
esp = serial.Serial(port,baund_rate,timeout=1)

def send_data(nunmber):
    command = f"{nunmber}\n"
    esp.write(command.encode('utf-8'))