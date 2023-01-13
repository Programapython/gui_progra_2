import folium as fl
import webbrowser
import funciones.funcionesGenerales as fng
import os


# CLASE QUE GENERA UN NUEVO MAPA
class new_map():
    def __init__(self):
        #VERIFICAMOS LA DIRECCIÓN ACTUAL
        dir_actual=os.getcwd()

        #LEE LA CANTIDAD DE MAPAS QUE HAN SIDO CREADOS
        i = fng.doc("./documentos/data2.txt").operacion("LE")[0][1]
        i = int(i)+1

        #CREA EL MAPA EN LA DIRECCIÓN MOSTRADA
        direccion = dir_actual + f"\\documentos\\map_{i}.html"
        map = fl.Map(location=[-8.109212390285986, -79.02565702089997], zoom_start=15, control_scale=True)
        map.add_child(fl.Marker(location=[-8.105900, -80.073899], popup="VEHÍCULO 1"))
        map.save(direccion)

        #SE GUARDA LA CANTIDAD DE MAPAS CREADOS
        fng.cambiar_dato("./documentos/data2.txt",0,str(i))

        webbrowser.open(direccion)