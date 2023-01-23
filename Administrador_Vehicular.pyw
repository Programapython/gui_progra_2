import tkinter as tk
import threading
import funciones.funcionesGenerales as fng
from PIL import ImageTk, Image
from funciones.ventanas import *
import funciones.mapa as mapa
import funciones.conec_arduino as arduino

#CLASE QUE INICIALIAZ LA VENTANA PRINCIPAL DE LA APLICACIÓN

class ventana(ventana_base):
    def __init__ (self):
        self.wn=tk.Tk()
        self.wn.geometry("800x500")
        self.wn.title("SISTEMA DE CONTROL VEHICULAR")
        self.wn.iconbitmap("./imagenes/Micro.ico")

        if fng.buscar_doc2("tipo_fondo") == "imagen":
            imagen=Image.open(fng.buscar_doc2("fondo_pantalla"))
            imagen=imagen.resize((800,530), Image.ANTIALIAS)
            img=ImageTk.PhotoImage(imagen)
            self.label=tk.Label(self.wn, image=img)
            self.label.place(x=0,y=0)
        else:  
            self.wn.config(bg = fng.buscar_doc2("fondo_pantalla"))
        
        self.wn.resizable(0,0)
        self.botones()
        self.titulos()
        self.datos()
        self.tiempo()
        self.tabla()
        self.menu()
        self.mainloop()


    def botones(self):
        boton(self.wn,  "VER UNIDADES DETENIDAS", "dodger blue2").medida_posicion(200, 425, 310)
        boton(self.wn, "GENERAR REPORTE", "gold", lambda: vnt().generar_pdf()).medida_posicion(200, 425, 345)
        boton(self.wn, "EMITIR ALERTA VEHICULAR", "red").medida_posicion(200, 425, 380)
        boton(self.wn, "INICIAR OPERACIONES", "lawn green",lambda: ventana_agregar_datos(tablaexterna=self.Tabla).mainloop()).medida_posicion(200, 425, 415) 
    
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
        boton(self.Tabla.tkframe(), 'VER EN EL MAPA', 'grey', lambda: mapa.generar_mapa()).grid(1 , 3)
        boton(self.Tabla.tkframe(), 'TERMINAR LAS OPERACIONES', 'grey', lambda: vnt().terminar_op()).grid(1, 4)
        
        #VERIFICA SI HAY INFORMACIÓN GUARDADA PARA MOSTRAR EN LA TABLA
        #-------------------------------------------------------------
        #-------------------------------------------------------------
        d_grd = fng.doc().operacion('L')
        if d_grd != []:
            for i in d_grd:
                #ELIMINA EL ID_SALIDA DE LOS DATOS ENCONTRADOS
                del i[0]
                #---------------------------------------------
                self.Tabla.agregar_datos(i)
        #-------------------------------------------------------------
        #-------------------------------------------------------------

        self.Tabla.posicionar()

    def menu(self):
        #FUNCIONES QUE SE USARAN DESPUES
        def nuevaventana(event=None):
            if fng.buscar_doc2("tipo_fondo") == "imagen":
                messagebox.showerror(title="ERROR AL ABRIR UNA NUEVA VENTANA", 
                message="No se pueden abrir nuevas pestañas cuando se tiene como fondo de pantalla una imagen.")
            else:
                ventana()
        def terminar_op(event=None):
            vnt().terminar_op()
        
        menu1=menubar(self.wn)
        menu1.titulos1('Opciones', 'Herramientas', 'configuración', 'Ayuda')
        menu1.titulos2(1,'Nueva ventana', nuevaventana, 'Ctrl+N')
        self.wn.bind_all("<Control-n>", nuevaventana)
        menu1.titulos2(1,'Modo oscuro', lambda: self.wn.config(bg='grey'))
        menu1.titulos2(1,'Modo claro', lambda: self.wn.config(bg='white'))
        menu1.separador(1)
        menu1.titulos2(1,'Terminar operaciones', terminar_op, 'Ctrl+T')
        self.wn.bind_all("<Control-t>", terminar_op)
        menu1.separador(1)
        menu1.titulos2(1,'Salir', self.wn.destroy)
        #----------------------------------------------------------------------------
        menu1.titulos2(2,'Generar informe')
        menu1.titulos2(2,'Generar mapa', lambda: mapa.generar_mapa())
        #----------------------------------------------------------------------------
        menu1.titulos2(3,'Modificar apariencia',lambda: vnt().ventana_fondo(self.wn))
        menu1.titulos2(3,'Configurar mapas', lambda: vnt().ventana_modificar_mapas())
        menu1.separador(3)
        menu1.titulos2(3,'Configurar conexion arduino', lambda: vnt().ventana_modificar_mapas())
        #----------------------------------------------------------------------------
        menu1.titulos2(4, 'Ayuda')
        menu1.separador(4)
        menu1.titulos2(4, 'Acerca de ...', lambda: vnt().acerca_de())

        self.wn.geometry("800x530")
    


# EJECUCUIÓN DE LA INTERFAZ
def generar_app():
    vn = ventana()

def leer_arduino():
    while True:
        if fng.buscar_doc2("operaciones_iniciadas") == "si":
            print("estoy accediendo")
            arduino.c_arduino().leer_llegada()

if __name__ == "__main__":
    hilo_app = threading.Thread(target=generar_app)
    hilo_app.start()
    hilo_arduino = threading.Thread(target=leer_arduino, daemon=True)
    hilo_arduino.start()