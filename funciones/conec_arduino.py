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
        time.sleep(2)
        self.conec.write(hora_asignada.encode("ascii"))
    
    def leer_llegada(self):
        bandera_llegada=self.conec.readline()
        if bandera_llegada.decode() != None:
            id_salida = bandera_llegada
            fng.modificar_salida(id_salida)
            print("llegue")
            

