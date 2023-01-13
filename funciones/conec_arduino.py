import serial as py
import threading
import time

class c_arduino():
    def __init__(self):
        self.conec=py.serial("COM4",9600)
        self.conec.write()
    
    def leer_llegada(self):
        hora_llegada=self.conec.read(100)
        self.close()
        return hora_llegada

    def escribir_tiempo_faltante(self):
        self.conec.read()