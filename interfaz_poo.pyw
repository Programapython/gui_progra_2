import tkinter as tk
from tkinter import ttk
import funciones.funciones1 as func1
import time
import cnmysql.conec_sql as conec

#CLASE QUE GENERA UN FRAME EN LA VENTANA
class espacio():
    def __init__(self, wn, color, pox, poy, base=10, altura=10):
        self.frame=tk.Frame(wn, bg=color)
        self.frame.config(width=base, height=altura)
        self.frame.place(x=pox, y=poy)

#GENERA UNA SUBVENTANA
class subventana():
    def __init__(self, wn, color, pox, poy, base=10, altura=10):
        self.subv=wn.Toplevel(wn, bg=color)
        self.frame.config(width=base, height=altura)
        self.frame.place(x=pox, y=poy)


#CLASE QUE GENERA UN BOTÓN
class boton():
    def __init__(self, wn, pox=0, poy=0, texto = 'texto predefinido', color='white', cmd=None):
        self.bt= tk.Button(wn, text = texto, bg = color, command=cmd)
        self.bt.place(x = pox, y = poy)

    def medida(self, base, altura=30):
        self.bt.place(width=base, height=altura)


#CLASE QUE GENERA CUADROS DE TEXTO ESTÁTICO 
class titulo():
    def __init__(self, wn, pox=0, poy=0, contenido = 'texto predefinido', colorL = 'cyan', colorC='black'):
        self.tl = tk.Label(wn, text = contenido ,fg = colorL, bg = colorC)
        self.tl.place(x = pox, y = poy)

    def medida(self, base, altura=30):
        self.tl.place(width=base, height=altura)

#CLASE QUE GENERA CUADROS PARA INGRESAR DATOS
class dato():
    def __init__(self, wn, pox, poy, informacion, base=50, altura=30):
        self.dt=tk.Label(wn, text=informacion, fg="black", bg="cyan", font = ("Tahoma", 15))
        self.dt.place(x=pox, y=poy, width=base, height=altura)


#CLASE QUE GENERA CUADROS DE TEXTO PARA COMPLETAR
class cuadro_editor():
    def __init__(self, wn, pox, poy, base=50, altura=30, vartex=None):
        self.ce=tk.Entry(wn, fg="black", bg="cyan", font = ("Tahoma", 15), textvariable=vartex)
        self.ce.place(x=pox, y=poy, width=base, height=altura)


#CLASE QUE GENERA LA HORA Y LA FECHA DE LA APLICACIÓN
class fecha_hora():
    def __init__(self,wn):
        
        titulo(wn, 425, 460, "FECHA").medida(50, 30)
        fecha=tk.Label(wn, text=time.strftime('%d/%m/%y'), fg="black", bg="cyan", font = ("Tahoma", 15))
        fecha.place(x=480, y=460, width=120, height=30)
        
        titulo(wn, 620, 460, "HORA").medida(50, 30)
        hora=tk.Label(wn, text=time.strftime('%H:%M:%S'), fg="black", bg="cyan", font = ("Tahoma", 15))
        hora.place(x=675, y=460, width=100, height=30)

        def reloj():
            hora_actual = time.strftime('%H:%M:%S') 
            if hora["text"] != hora_actual:
                hora["text"] = hora_actual
            wn.after(100, reloj)
        
        reloj()

#CLASE QUE GENERA UNA TABLA
class table():
    def __init__(self, wn, nColumnas, encabezados):
        self.sp=tk.Frame(wn, bg='black')
        self.sp.config(width=10, height=10)
        self.sp.place(x=40, y=120)
        columnas=[]

        for i in range(nColumnas-1):
            columnas.append('col{}'.format(i+1))

        self.tbl=ttk.Treeview(self.sp, columns=columnas)
        
        for i in range(nColumnas):
            if i == 0:
                self.tbl.column('#0'.format(i), width=100, anchor="center")
                self.tbl.heading('#0', text=encabezados[0], anchor="center")
            else:
                self.tbl.column(f'col{i}', width=100, anchor="center")
                self.tbl.heading(f'col{i}', text=encabezados[i], anchor="center")
    
    def agregar_datos(self, datos):
        self.tbl.insert("","end", text=datos.pop(0), values=datos)
    
    def boton(self, texto, color, cl= 1, rw= 2 , pox=10, poy=10, comando=None):
        tk.Button(self.sp, text = texto, bg = color).grid(column=cl, row=rw, padx=pox, pady=poy, command=comando)

    def grid(self):
        self.tbl.grid(column=1, row=1, padx=10, pady=10)
    
#CLASE QUE CREA UN MENÚ
class menubar():
    def __init__(self, wn):
        #Declara la ventana
        self.ventana=wn
        #Crea un menú
        self.m=tk.Menu(self.ventana)
        #se agrega el menú a la ventana que se le pasa como parámetro
        self.ventana.config(menu=self.m)
        #Lista de los titulos1
        self.t1=[]

    def titulos1(self, *nombres):
        #crea el los submenús del menú, estos se obtienen de la lista nombres
        #El tearoff indica que no se muestre -- al abrir un submenú
        for n in nombres:
            elemento=tk.Menu(self.m, tearoff=0)
            self.m.add_cascade(label=n, menu=elemento)
            self.t1.append(elemento)

    def titulos2(self, posicion, nombre, nombre_comando="", atajo=""):
        #crea un elemento del submenú, este se obtiene del parámetro normbre
        #n indica la posición del submenú al cual se le van a añadir los elementos

        #Funciones:
        def cambiar_color_negro(event=None):
            self.ventana.config(bg='black')
        def cambiar_color_blanco(event=None):
            self.ventana.config(bg='white')
        def cambiar_color_gris(event=None):
            self.ventana.config(bg='grey')
        def salir(event=None):
            self.ventana.quit()
        def nuevaVentana(event=None):
            vn=ventana()
            vn.botones()
            vn.titulos()
            vn.datos()
            vn.tiempo()
            vn.tabla()
            vn.menu()
            vn.mainloop()   
        def sin_comando(event=None):
            print('No existe ningún comando')

        #Convertir el nombre_comando de string a función:
        if nombre_comando == 'cambiar_color_negro':
            nombre_comando = cambiar_color_negro
        elif nombre_comando == 'cambiar_color_blanco':
            nombre_comando = cambiar_color_blanco
        elif nombre_comando == 'cambiar_color_gris':
            nombre_comando = cambiar_color_gris
        elif nombre_comando == 'salir':
            nombre_comando = salir
        elif nombre_comando == 'nuevaVentana':
            nombre_comando = nuevaVentana
        else:
            nombre_comando = sin_comando
        
        #Agregar el nuevo submenpu y el comando correspondiente
        self.t1[posicion-1].add_command(label=nombre, accelerator=atajo, command=nombre_comando) 
        
        if atajo =='Ctrl+N':
            self.ventana.bind_all("<Control-n>", nombre_comando)
    
    def separador(self, posicion):
        self.t1[posicion-1].add_separator()
    

#CLASE QUE INICIALIAZ LA VENTANA PRINCIPAL

class ventana():
    def __init__ (self):
        self.wn=tk.Tk()
        self.wn.geometry("800x500")
        self.wn.title("SISTEMA DE CONTROL VEHICULAR")
        self.wn.iconbitmap("./images/Micro.ico")
        self.wn.config(bg = "gray")
        self.wn.resizable(0,0)

    def botones(self):
        def crear_nueva_ventana(event=None):
            vnt=ventana_nueva("400x220", "INICIALIZADOR DE OPERACIONES")
            vnt.datos()
            vnt.mainloop()
    
        boton(self.wn, 425, 310, "VER UNIDADES DETENIDAS", "dodger blue2").medida(200)
        boton(self.wn, 425, 345, "GENERAR REPORTE", "gold").medida(200)
        boton(self.wn, 425, 380, "EMITIR ALERTA VEHICULAR", "red").medida(200)
        boton(self.wn, 425, 415, "INICIAR OPERACIONES", "lawn green",crear_nueva_ventana).medida(200) 
    
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
        Tabla=table(self.wn, 3, ['ID_VEHICULO','RUTA','CHOFER'])
        for i in conec.datos_tabla1():
            Tabla.agregar_datos(i)
        Tabla.boton('VER DATOS COMPLETOS', 'grey')
        Tabla.boton('VER EN EL MAPA', 'grey', 1 , 3)

        Tabla.grid()
    
    def menu(self):
        
        menu1=menubar(self.wn)
        menu1.titulos1('Opciones', 'Herramientas', 'configuración', 'Ayuda')
        menu1.titulos2(1,'Nueva ventana', 'nuevaVentana', 'Ctrl+N')
        menu1.titulos2(1,'Modo oscuro', 'cambiar_color_negro')
        menu1.titulos2(1,'Modo claro', 'cambiar_color_blanco')
        menu1.titulos2(1,'Modo normal', 'cambiar_color_gris')
        menu1.separador(1)
        menu1.titulos2(1,'Salir', 'salir')
        menu1.titulos2(4, 'Ayuda')
        menu1.separador(4)
        menu1.titulos2(4, 'Acerca de ...')

        self.wn.geometry("800x530")

    def mainloop(self):
        self.wn.mainloop()

#CLASE QUE GENERA UNA NUEVA VENTANA:

class ventana_nueva (ventana):
    def __init__(self, geo="800x500", tl="SISTEMA DE CONTROL VEHICULAR", icon="./images/Micro.ico"):
        self.wn=tk.Toplevel()
        self.wn.geometry(geo)
        self.wn.title("INICIALIZADOR DE OPERACIONES")
        self.wn.iconbitmap(icon)
        self.wn.config(bg = "gray")
        self.wn.resizable(0,0)
    
    
    def datos(self):
        self.parameto1=tk.StringVar()

        titulo(self.wn, 65, 20, "VEHÍCULO").medida(100,30)
        cuadro_editor(self.wn, 185, 20, 150, 30)
        titulo(self.wn, 65, 55, "RUTA").medida(100,30)
        cuadro_editor(self.wn, 185, 55, 150, 30)
        titulo(self.wn, 65, 90, "CHOFER").medida(100,30)
        cuadro_editor(self.wn, 185, 90, 150, 30)
        titulo(self.wn, 65, 125, "HORA").medida(100,30)
        cuadro_editor(self.wn, 185, 125, 150, 30, self.parameto1)
        boton(self.wn, 50, 170, "ENVIAR", "grey", cmd=lambda:print(self.parameto1.get())).medida(100)
        boton(self.wn, 250, 170, "FINALIZAR", "grey").medida(100)

# EJECUCUIÓN DE LA INTERFAZ
vn=ventana()
vn.botones()
vn.titulos()
vn.datos()
vn.tiempo()
vn.tabla()
vn.menu()
vn.mainloop()
        

