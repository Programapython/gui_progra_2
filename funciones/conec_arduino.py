import funciones.funcionesGenerales as fng
import serial
import time

class c_arduino():
    def __init__(self):
        self.conec=serial.Serial(fng.buscar_doc2("nombre_puerto_arduino"),9600)

    def asignar_hora_salida(self, vehiculo=1):
        data_vehiculo=fng.doc().operacion("L")[vehiculo-1]
        hora_asignada=data_vehiculo[4]
        hora_asignada=hora_asignada[:2]
        time.sleep(2)
        self.conec.write(hora_asignada.encode("ascii"))
        self.conec.close()
    
    def leer_llegada(self):
        bandera_llegada=self.conec.readline()
        if bandera_llegada.decode() != None:
            id_salida = bandera_llegada
            fng.modificar_salida(id_salida)
            print("llegue")
            

