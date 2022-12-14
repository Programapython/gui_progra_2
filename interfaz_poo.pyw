import tkinter as tk
import funciones.funcionesGenerales as fng
from funciones.ventanas import boton, titulo, dato, fecha_hora, table, menubar, ventana_base, ventana_agregar_datos, vnt

#CLASE QUE INICIALIAZ LA VENTANA PRINCIPAL DE LA APLICACIÓN

class ventana(ventana_base):
    def __init__ (self):
        self.wn=tk.Tk()
        self.wn.geometry("800x500")
        self.wn.title("SISTEMA DE CONTROL VEHICULAR")
        self.wn.iconbitmap("./images/Micro.ico")
        self.wn.config(bg = "gray")
        self.wn.resizable(0,0)
        self.botones()
        self.titulos()
        self.datos()
        self.tiempo()
        self.tabla()
        self.menu()
        self.mainloop()
        

    def pestaña_agregar_datos(self):
        ventana_agregar_datos(tablaexterna=self.Tabla).mainloop()

    def botones(self):
        boton(self.wn,  "VER UNIDADES DETENIDAS", "dodger blue2").medida_posicion(200, 425, 310)
        boton(self.wn, "GENERAR REPORTE", "gold").medida_posicion(200, 425, 345)
        boton(self.wn, "EMITIR ALERTA VEHICULAR", "red").medida_posicion(200, 425, 380)
        boton(self.wn, "INICIAR OPERACIONES", "lawn green",self.pestaña_agregar_datos).medida_posicion(200, 425, 415) 
    
    def titulos(self):
        titulo(self.wn, 250, 20, "SOFTWARE DE RASTREO Y CONTROL").medida(250,40)
        titulo(self.wn, 400, 80, "DATOS GENERALES:").medida(150, 30)
        titulo(self.wn, 425, 135, "VEHÍCULOS EN CIRCULACIÓN").medida(200, 30)
        titulo(self.wn, 425, 170, "VEHÍCULOS NO CIRCULACIÓN").medida(200,30)
        titulo(self.wn, 425, 205, "VEHÍCULOS FUERA DE SERVICIO").medida(200,30) 
        titulo(self.wn, 425, 240, "VEHÍCULOS TOTALES").medida(200, 30)
        titulo(self.wn, 425, 275, "N° UNIDADES DETENIDAS").medida(200, 30)
    
    def datos(self):
        dato(self.wn, 630, 135, "")
        dato(self.wn, 630, 170, "")
        dato(self.wn, 630, 206, "")
        dato(self.wn, 630, 240, "")
        dato(self.wn, 630, 275, "")

    def tiempo(self):
        fecha_hora(self.wn)

    def tabla(self):
        self.Tabla=table(self.wn, 3, ['ID_VEHICULO','RUTA','CHOFER'])
        boton(self.Tabla.tkframe(), 'VER DATOS COMPLETOS', 'grey').grid(1, 2)
        boton(self.Tabla.tkframe(), 'VER EN EL MAPA', 'grey').grid(1 , 3)
        boton(self.Tabla.tkframe(), 'TERMINAR LAS OPERACIONES', 'grey', lambda: fng.doc().operacion("B")).grid(1, 4)
        

        #VERIFICA SI HAY INFORMACIÓN GUARDADA PARA MOSTRAR EN LA TABLA
        if fng.doc().operacion("L") != []:
            for i in fng.doc().operacion('L'):
                self.Tabla.agregar_datos(i)
        #----------------------------------------------------------------

        self.Tabla.posicionar()

    def menu(self):
        
        menu1=menubar(self.wn)
        menu1.titulos1('Opciones', 'Herramientas', 'configuración', 'Ayuda')
        menu1.titulos2(1,'Nueva ventana', lambda: ventana(), 'Ctrl+N')
        menu1.titulos2(1,'Modo oscuro', lambda: self.wn.config(bg='black'))
        menu1.titulos2(1,'Modo claro', lambda: self.wn.config(bg='white'))
        menu1.titulos2(1,'Modo normal', lambda: self.wn.config(bg='grey'))
        menu1.separador(1)
        menu1.titulos2(1,'Salir', 'salir')
        menu1.titulos2(4, 'Ayuda')
        menu1.separador(4)
        menu1.titulos2(4, 'Acerca de ...', lambda: vnt().acerca_de())

        self.wn.geometry("800x530")
    


# EJECUCUIÓN DE LA INTERFAZ
vn=ventana()


        

