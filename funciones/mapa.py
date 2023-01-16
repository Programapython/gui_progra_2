import folium as fl
from folium.plugins import MarkerCluster, MousePosition
import webbrowser
import pandas as pd
import os
import funciones.funcionesGenerales as fng



# CLASE QUE GENERA UN NUEVO MAPA
class map():
    def __init__(self):
        #VERIFICAMOS LA DIRECCIÓN ACTUAL
        dir_actual=os.getcwd()

        #LEE LA CANTIDAD DE MAPAS QUE HAN SIDO CREADOS
        i = fng.buscar_doc2("numero_mapas")
        i = int(i)+1

        #SE GUARDA LA CANTIDAD DE MAPAS CREADOS
        fng.cambiar_doc2("numero_mapas",str(i))

        #CREA LA DIRECCIÓN PARA GUARDAR EL MAPA
        self.direccion = dir_actual + f"\\documentos\\mapas\\map_{i}.html"

        #SE CREA EL MAPA
        self.map = fl.Map(location=[-8.10921, -79.02565], zoom_start=15, control_scale=True, min_zoom=13)
        self.mc = MarkerCluster()
        #-------------------------------------------------------------------------------------------
        self.icono_inicio=fl.Icon(color='blue',icon='building', icon_color='black', prefix='fa')
        self.icono_bus=fl.Icon(color='green',icon='bus', icon_color='black', prefix='fa')
        #-------------------------------------------------------------------------------------------
        
        
        self.marcador_inicio=fl.Marker(location=[-8.10321, -79.01778], popup="PUNTO INICIO|FINAL", icon=self.icono_inicio)
        self.marcador_bus=fl.Marker(location=[-8.10321, -79.02778], popup="BUS 1", icon=fl.Icon(color='green',icon='bus', icon_color='black', prefix='fa'))
        self.marcador_bus2=fl.Marker(location=[-8.10321, -79.03778], popup="BUS 2", icon=fl.Icon(color='green',icon='bus', icon_color='black', prefix='fa'))
        fmtr = "function(num) {return L.Util.formatNum(num, 5) + ' º ';};"
        mp=MousePosition(position='topright', separator=' | ', prefix="Posición Actual:", lat_formatter=fmtr, lng_formatter=fmtr)


        self.map.add_child(self.marcador_inicio)
        self.map.add_child(mp)
        

    
    def new_ruta(self, nombre_ruta="Sin ruta"):

        #SE CREA UNA NUEVA RUTA
        #-------------------------------------------------------------------------------------------
        self.rutaX=fl.FeatureGroup(name=f"RUTA {nombre_ruta}")
        #-------------------------------------------------------------------------------------------
        pd.options.display.max_rows = 1000
        paraderos=pd.read_csv('./documentos/paraderos.csv')
        paraderos.query(f"ruta == '{nombre_ruta}'")
        latitudes=paraderos['latitud'].to_list()
        longitudes=paraderos['longitud'].to_list()
        numero=paraderos['numero_paradero'].to_list()
        
        for lat, lon, indice in zip(latitudes, longitudes, numero):
            Lat=float(lat)
            Lon=float(lon)
            #PARADEROS RUTA A
            #---------------------------------------------------------------------------------------------------
            icono_paradero=fl.Icon(color='beige',icon='person', icon_color='black', prefix='fa')
            fl.Marker(location=[Lat, Lon], popup=f'PARADERO {indice}', icon=icono_paradero).add_to(self.rutaX)
            #---------------------------------------------------------------------------------------------------
        
        self.map.add_child(self.rutaX)
        self.map.add_child(fl.LayerControl())

    def marcador(self):
        self.mc.add_child(self.marcador_bus)
        self.mc.add_child(self.marcador_bus2)
        self.map.add_child(self.mc)
    
    def mostrar_mapa(self):
        self.map.save(self.direccion)
        webbrowser.open(self.direccion)

def new_map():
    m=map()
    m.marcador()
    m.new_ruta("A")
    m.mostrar_mapa()

