import mysql.connector
from mysql.connector import Error
import funciones.funcionesGenerales as fng
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python

#CLASE QUE GENERA UNA CONEXIÓN CON MYSQL
class conexion_msql():
    def __init__(self, pedido=""):
        self.data=[]
        try:
            clave='MgB1Q9529nub9HEjggLr'
            usuario='urd2jbllb60jvsko'
            self.conexion=mysql.connector.connect(user=f"{usuario}", password=f"{clave}", 
                                            host='bwrgomsofdlj6yeoge45-mysql.services.clever-cloud.com',
                                            database='bwrgomsofdlj6yeoge45',
                                            port='3306')

            self.solicitud(pedido)

            self.conexion.close()

        except Error as error:
            print(error)
    
    def solicitud(self, comando):
        cursor=self.conexion.cursor()
        cursor.execute(comando)
        
        for i in cursor:
            self.data.append(list(i))
    
    def verificar_data(self):
        if self.data == []:
            return "No se ha encontrado data, vuelve a realizar la petición"
        else:
            return self.data

# FUNCIONES PARA LEER DATOS

def verificar_contraseña(contra):
    return conexion_msql(f'''CALL buscar_contraseña('{contra}')''').verificar_data()


# FUNCIONES PARA AGREGAR DATOS

def enviar_datos_tabla():
    lista_datos = fng.doc().operacion("L")
    pedido = ''''''
    for dato in lista_datos:
        pedido+=f'''INSERT INTO `Trayectoria_Vehículo` (`ID_Vehiculo`, `Ruta`, `ID_Chofer`, `Hora_Salida`, `dia_salida`, `marca_1`, `vel_1`, `marca_2`, `vel_2`, `marca_3`, `vel_3`, `marca_llegada`) 
                                           VALUES ('{dato[1]},'{dato[2]}','{dato[3]}','{dato[4]}','{dato[5]}','{dato[6]}','{dato[7]}','{dato[8]}','{dato[9]}','{dato[10]}','{dato[11]}','{dato[12]}');'''
        
    conexion_msql(pedido).verificar_data()

