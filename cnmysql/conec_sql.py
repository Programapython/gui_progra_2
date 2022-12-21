import mysql.connector
from mysql.connector import Error 
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python

clave='MgB1Q9529nub9HEjggLr'
usuario='urd2jbllb60jvsko'

class conexion():
    def __init__(self, comando):
        try:
            self.conexion=mysql.connector.connect(user=f'{usuario}', password=f"{clave}", 
                                            host='bwrgomsofdlj6yeoge45-mysql.services.clever-cloud.com',
                                            database='bwrgomsofdlj6yeoge45',
                                            port='3306')
        except Error as error:
            return print(error)
    
    def solicitud(self,)
            cursor=self.conexion.cursor()
            cursor.execute(comando)
            return cursor
        

    def close(self):
        self.conexion.close()


def dataPrincipal():
    conexion("SELECT * FROM directivos").close()


dataPrincipal()
