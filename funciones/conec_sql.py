import mysql.connector
from mysql.connector import Error 
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python


class conexion():
    def __init__(self):
        try:
            clave='MgB1Q9529nub9HEjggLr'
            usuario='urd2jbllb60jvsko'
            self.conexion=mysql.connector.connect(user=f"{usuario}", password=f"{clave}", 
                                            host='bwrgomsofdlj6yeoge45-mysql.services.clever-cloud.com',
                                            database='bwrgomsofdlj6yeoge45',
                                            port='3306')
        except Error as error:
            print(error)
    
    def solicitud(self, comando):
        data=[]
        cursor=self.conexion.cursor()
        cursor.execute(comando)
        
        for i in cursor:
            data.append(list(i))
        
        return data

    def close(self):
        self.conexion.close()


def datos_tabla1():
    cnx=conexion()
    data=cnx.solicitud("SELECT id_Vehículo, ruta, Nombre FROM Vehículo v LEFT JOIN Chofer c ON c.id=v.id_Vehículo LEFT JOIN Trayectoria_vehiculo t ON c.id=t.Vehículo_Chofer_id")
    cnx.close()
    return data



