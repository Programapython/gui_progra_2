import mysql.connector
from mysql.connector import Error 
#Comando para descargar el modeulo de conexión con mysql
#pip install mysql-connector-python

clave='MgB1Q9529nub9HEjggLr'
usuario='urd2jbllb60jvsko'
try:
    conexion=mysql.connector.connect(user=f'{usuario}', password=f"{clave}", 
                                    host='bwrgomsofdlj6yeoge45-mysql.services.clever-cloud.com',
                                    database='bwrgomsofdlj6yeoge45',
                                    port='3306')

    cursor=conexion.cursor()
    cursor.execute('SELECT Nombre, id_Vehículo FROM Chofer c INNER JOIN Vehículo v ON c.id=v.Chofer_id;')
    for fila in cursor:
        print(fila)
    conexion.close()

except Error as error:
    print(f"Ha ocurrido un error:{error}")
