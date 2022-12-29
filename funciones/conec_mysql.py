import mysql.connector
from mysql.connector import Error 
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python

#PEDIDOS:

datos_tabla = '''SELECT id_Vehículo, ruta, Nombre FROM Vehículo v LEFT JOIN 
Chofer c ON c.id=v.id_Vehículo LEFT JOIN Trayectoria_vehiculo t ON c.id=t.Vehículo_Chofer_id'''


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

            self.verificar_data()

        except Error as error:
            return error
    
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


def datos_tabla_principal():
    conexion_msql(datos_tabla)

def verificar_contraseña():
    pass



