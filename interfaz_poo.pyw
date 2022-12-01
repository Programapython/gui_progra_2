import tkinter as tk
from tkinter import ttk
import time

#CLASE QUE GENERA UN FRAME EN LA VENTANA
class espacio():
    def __init__(self, wn, color, pox, poy, base=10, altura=10):
        self.frame=tk.Frame(wn, bg=color)
        self.frame.config(width=base, height=altura)
        self.frame.place(x=pox, y=poy)

#CLASE QUE GENERA UN BOTÓN
class boton():
    def __init__(self, wn, pox=0, poy=0, texto = 'texto predefinido', color='white'):
        self.bt= tk.Button(wn, text = texto, bg = color)
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
        dt=tk.Label(wn, text=informacion, fg="black", bg="cyan", font = ("Tahoma", 15))
        dt.place(x=pox, y=poy, width=base, height=altura)


#CLASE QUE GENERA CUADROS DE TEXTO PARA COMPLETAR
'''Por implementar'''


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
            wn.after(500, reloj)
        
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
                self.tbl.column('col{}'.format(i), width=100, anchor="center")
                self.tbl.heading('col{}'.format(i), text=encabezados[i], anchor="center")
    
    def agregar_datos(self, datos):
        self.tbl.insert("","end", text=datos.pop(0), values=datos)
    
    def boton(self, texto, color):
        tk.Button(self.sp, text = texto, bg = color).grid(column=1, row=2, padx=10, pady=30)


    def grid(self):
        self.tbl.grid(column=1, row=1, padx=10, pady=10)
    


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
        boton(self.wn, 425, 310, "VER UNIDADES DETENIDAS", "dodger blue2").medida(200)
        boton(self.wn, 425, 345, "GENERAR REPORTE", "gold").medida(200)
        boton(self.wn, 425, 380, "EMITIR ALERTA VEHICULAR", "red").medida(200)
        boton(self.wn, 425, 415, "INICIAR OPERACIONES", "lawn green").medida(200) 
    
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

    def tabla(self,n_vehiculos):
        Tabla=table(self.wn, 3, ['ID_VEHICULO','RUTA','POSICIÓN'])
        for i in range(n_vehiculos):
            Tabla.agregar_datos([str(i+1),'A'+str(i+1), 'PARADERO '+str(i+1)])
        Tabla.boton('VER DATOS COMPLETOS', 'blue')
        Tabla.grid()
    
    def mainloop(self):
        self.wn.mainloop()

    
# EJECUCUIÓN DE LA INTERFAZ
vn=ventana()
vn.botones()
vn.titulos()
vn.datos()
vn.tiempo()
vn.tabla(100)
vn.mainloop()
        

