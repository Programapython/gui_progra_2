import mysql.connector
from mysql.connector import Error
import funciones.funcionesGenerales as fng
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python

#CLASE QUE GENERA UNA CONEXIÓN CON MYSQL
class conexion_msql():
    def __init__(self,clase_pedido = "leer",  pedido=""):
        self.data=[]
        self.clase_pedido = clase_pedido
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
        if self.clase_pedido == "leer":
            for dato in cursor:
                self.data.append(list(dato))
        elif self.clase_pedido == "insertar":
            self.conexion.commit()

    
    def verificar_data(self):
        if self.data == []:
            return "No se ha encontrado data, vuelve a realizar la petición"
        else:
            return self.data

# FUNCIONES PARA LEER DATOS

def verificar_contraseña(contra):
    return conexion_msql(pedido=f'''CALL buscar_contraseña('{contra}')''').verificar_data()

def recibir_datos_tabla(fecha = None):
    m='''SELECT * FROM Trayectoria_Vehículo '''
    if fecha != None:
        m+=f'''WHERE dia_salida = '{fecha}' '''
    m+=''';'''
    return conexion_msql(pedido=m).verificar_data()


# FUNCIONES PARA AGREGAR DATOS

def enviar_datos_tabla():
    lista_datos = fng.doc().operacion("L")
    pedido = ''''''
    for linea in lista_datos:
        pedido+=f'''INSERT INTO `Trayectoria_Vehículo` (`ID_Vehiculo`, `Ruta`, `ID_Chofer`, `Hora_Salida`, `dia_salida`, `marca_1`, `vel_1`, `marca_2`, `vel_2`, `marca_3`, `vel_3`,`marca_llegada`) 
                VALUES ({linea[1]},'{linea[2]}',{linea[3]},'{linea[4]}','{linea[5]}','{linea[6]}',{linea[7]},'{linea[8]}',{linea[9]},'{linea[10]}','{linea[11]}','{linea[12]}');'''
        print(pedido)
    conexion_msql("insertar",pedido)