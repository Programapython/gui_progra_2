import mysql.connector
from mysql.connector import Error 
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python

#PEDIDOS:

enviar_datos_tabla = lambda datos_ingresados: "INSERT INTO `Trayectoria_Vehículo` (`ID_Vehiculo`, `Ruta`, `ID_Chofer`, `Hora_Salida`, `dia_salida`, `marca_1`, `vel_1`, `marca_2`, `vel_2`, `marca_3`, `vel_3`, `marca_llegada`) VALUES ({datos_ingresados});"

buscar_contraseña =lambda i: f'''CALL buscar_contraseña('{i}')'''

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

def datos_tabla_principal(lista_datos):
    for dato in lista_datos:
        return conexion_msql(enviar_datos_tabla(i)).verificar_data()

def verificar_contraseña(contraseña):
    return conexion_msql(buscar_contraseña(contraseña)).verificar_data()

# FUNCIONES PARA AGREGAR DATOS

def agregar_datos_tabla_principal():
    pass


