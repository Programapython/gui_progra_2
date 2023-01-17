import folium as fl
from folium.plugins import MarkerCluster, MousePosition
import webbrowser
import pandas as pd
import os
import time
import funciones.funcionesGenerales as fng



# CLASE QUE GENERA UN NUEVO MAPA
class map():
    def __init__(self):
        #VERIFICAMOS LA DIRECCIÓN ACTUAL
        dir_actual=os.getcwd()

        #LEE LA CANTIDAD DE MAPAS QUE HAN SIDO CREADOS
        i = fng.buscar_doc2("numero_mapas")
        i = int(i)+1
        self.paraderos = []

        #SE GUARDA LA CANTIDAD DE MAPAS CREADOS
        fng.cambiar_doc2("numero_mapas",str(i))

        #CREA LA DIRECCIÓN PARA GUARDAR EL MAPA
        self.direccion = dir_actual + f"\\documentos\\mapas\\map_{i}.html"

        #SE CREA EL MAPA
        self.map = fl.Map(location=[-8.10921, -79.02565], zoom_start=15, control_scale=True, min_zoom=10)
        self.terminales=fl.FeatureGroup(name="Terminales")
        #-------------------------------------------------------------------------------------------
        self.icono_inicio=fl.Icon(color='blue',icon='building', icon_color='black', prefix='fa')
        #-------------------------------------------------------------------------------------------
        self.c_inicio = [-8.10321, -79.01778]
        self.terminal1=fl.Marker(location=self.c_inicio, popup="PUNTO INICIO|FINAL", icon=self.icono_inicio)
        self.terminal1.add_to(self.terminales)

        fmtr = "function(num) {return L.Util.formatNum(num, 5) + ' º ';};"
        mp=MousePosition(position='topright', separator=' | ', prefix="Posición Actual:", lat_formatter=fmtr, lng_formatter=fmtr)

        self.map.add_child(self.terminales)
        self.map.add_child(mp)


    
    def new_ruta(self, raiz=None, nombre_ruta="Sin ruta"):

        pd.options.display.max_rows = 100
        paraderos=pd.read_csv('./documentos/paraderos.csv')
        paraderos.query(f"ruta == '{nombre_ruta}'")
        latitudes=paraderos['latitud'].to_list()
        longitudes=paraderos['longitud'].to_list()
        numero=paraderos['numero_paradero'].to_list()
            
        for lat, lon, indice in zip(latitudes, longitudes, numero):
            Lat=float(lat)
            Lon=float(lon)
            self.paraderos.insert(int(indice)-1,[Lat, Lon])
            #PARADEROS RUTA A
            #---------------------------------------------------------------------------------------------------
            if raiz == None:
                icono_paradero=fl.Icon(color='beige',icon='person', icon_color='black', prefix='fa')
                fl.Marker(location=[Lat, Lon], popup=f'PARADERO {indice}', icon=icono_paradero).add_to(self.map)
            else:
                icono_paradero=fl.Icon(color='beige',icon='person', icon_color='black', prefix='fa')
                fl.Marker(location=[Lat, Lon], popup=f'PARADERO {indice}', icon=icono_paradero).add_to(raiz)
            #---------------------------------------------------------------------------------------------------

            
    def new_vehiculos(self, raiz=None, nombre_ruta="Sin ruta"):

        vehiculos = pd.read_csv('./documentos/data.txt')
        vehiculos.query(f"RUTA == '{nombre_ruta}'")
        nombres = vehiculos['ID_VEHICULO'].to_list()
        marcas1 = vehiculos['MARCA_1'].to_list()
        marcas2 = vehiculos['MARCA_2'].to_list()
        marcas3 = vehiculos['MARCA_3'].to_list()
        contador=0
        for nombre, marca1, marca2, marca3 in zip(nombres, marcas1, marcas2, marcas3):
            aumento = -0.00010+contador/10000
            contador+=1
            #VEHÍCULOS DE LA RUTA A
            #---------------------------------------------------------------------------------------------------
            if type(marca3) != float:
                localizacion = [float(self.paraderos[2][0])+aumento,float(self.paraderos[2][1])+aumento]
            elif type(marca2) != float:
                localizacion = [float(self.paraderos[1][0])+aumento,float(self.paraderos[1][1])+aumento]
            elif type(marca1) != float:
                localizacion = [float(self.paraderos[0][0])+aumento,float(self.paraderos[0][1])+aumento]
            else:
                localizacion = [self.c_inicio[0]+aumento,self.c_inicio[1]+aumento]

            if raiz == None:
                icono_bus=fl.Icon(color='green',icon='bus', icon_color='black', prefix='fa')
                fl.Marker(location=localizacion, popup=f"BUS {nombre}", icon=icono_bus).add_to(self.map)
            else:
                icono_bus=fl.Icon(color='green',icon='bus', icon_color='black', prefix='fa')
                fl.Marker(location=localizacion, popup=f"BUS {nombre}", icon=icono_bus).add_to(raiz)
                

        
    def new_ruta_con_vehiculos(self, nombre="Sin ruta"):

        #SE CREA UNA NUEVA RUTA
        #-------------------------------------------------------------------------------------------
        rutaX=fl.FeatureGroup(name=f"RUTA {nombre}")
        #-------------------------------------------------------------------------------------------
        self.new_ruta(raiz=rutaX, nombre_ruta=nombre)
        self.new_vehiculos(raiz=rutaX, nombre_ruta=nombre)
        
        self.map.add_child(rutaX)
        self.map.add_child(fl.LayerControl())

    def new_ruta_sin_vehiculos(self, nombre="Sin ruta"):
        #SE CREA UNA NUEVA RUTA Y UN NUEVO MARCADOR
        #-------------------------------------------------------------------------------------------
        rutaX=fl.FeatureGroup(name=f"RUTA {nombre}")
        mc = MarkerCluster(name=f"Vehiculos en operación | ruta {nombre}")
        #-------------------------------------------------------------------------------------------
        self.new_ruta(raiz=rutaX, nombre_ruta=nombre)
        self.new_vehiculos(raiz=mc, nombre_ruta=nombre)
        
        self.map.add_child(rutaX)
        self.map.add_child(mc)
        self.map.add_child(fl.LayerControl())
  
    def mostrar_mapa(self):
        self.map.save(self.direccion)
        webbrowser.open(self.direccion)


def generar_mapa():
    if fng.buscar_doc2("tipo_mapa") == "normal":
        m=map()
        m.new_ruta(nombre_ruta="A")
        m.new_vehiculos(nombre_ruta="A")
        m.mostrar_mapa()
    
    if fng.buscar_doc2("tipo_mapa") == "con_capas":
        m=map()
        m.new_ruta_con_vehiculos("A")
        m.mostrar_mapa()
    
    elif fng.buscar_doc2("tipo_mapa") == "con_marcador":
        m=map()
        m.new_ruta_sin_vehiculos("A")
        m.mostrar_mapa()
