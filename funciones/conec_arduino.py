import funciones.funcionesGenerales as fng
import serial as py
import threading
import time

class c_arduino():
    def __init__(self):
        self.conec=py.serial(fng.buscar_doc2("nombre_puerto_arduino"),9600)
        self.conec.write()
    
    def leer_llegada(self):
        hora_llegada=self.conec.read(100)
        self.close()
        return hora_llegada

    def escribir_tiempo_faltante(self):
        self.conec.read()