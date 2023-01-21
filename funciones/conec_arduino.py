import funciones.funcionesGenerales as fng
import serial
import threading
import time

class c_arduino():
    def __init__(self):
        self.conec=serial.Serial("COM16",9600)

    def asignar_hora_salida(self, vehiculo=1):
        data_vehiculo=fng.doc().operacion("L")[vehiculo-1]
        hora_asignada=data_vehiculo[4]
        print(hora_asignada)
        self.conec.write("hora_asignada".encode("ascii"))
        time.sleep(5)
        self.conec.close()

    def leer_llegada(self):
        hora_llegada=self.conec.read(100)
        self.close()
        return hora_llegada
    