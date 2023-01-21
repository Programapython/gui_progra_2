import funciones.funcionesGenerales as fng
import serial
import threading
import time

class c_arduino():
    def __init__(self):
        self.conec=serial.Serial("COM16",9600)

    def asignar_hora_salida(self, vehiculo=1):
        # data_vehiculo=fng.doc().operacion("L")[vehiculo-1]
        # hora_asignada=data_vehiculo[4]
        # print(hora_asignada)
        while True:
            self.conec.write('1'.encode())
            time.sleep(0.1)
            break

    def leer_llegada(self):
        hora_llegada=self.conec.readline()
        if hora_llegada.decode() == "1":
            print.time(time.strftime('%H:%M:%S'))
