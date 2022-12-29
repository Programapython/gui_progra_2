import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import funciones.funcionesGenerales as fncg
import time
import funciones.conec_mysql as conec

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
    def __init__(self, wn, pox, poy, base=50, altura=30, vartex=None, contraseña=False):
        if contraseña == False:
            self.ce=tk.Entry(wn, fg="black", bg="cyan", font = ("Tahoma", 15), textvariable=vartex)
        else:
            self.ce=tk.Entry(wn, fg="black", bg="cyan", font = ("Tahoma", 15), textvariable=vartex, show="*")
        
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
    def __init__(self, wn, nColumnas, encabezados, con_frame=True):
        self.opcion=con_frame
        if self.opcion == True:
            self.sp=tk.Frame(wn, bg='black')
            self.sp.config(width=10, height=10)
            self.sp.place(x=40, y=80)
        else:
            self.sp=wn

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
        self.tbl.insert("","end", text=datos[0], values=datos[1:len(datos)])
    
    def boton(self, texto, color, cl= 1, rw= 2 , pox=10, poy=10, comando=None):
        tk.Button(self.sp, text = texto, bg = color).grid(column=cl, row=rw, padx=pox, pady=poy, command=comando)

    def posicionar(self, columna=1, fila=1, pox=0, poy=0):
        if self.opcion == True:
            self.tbl.grid(column=columna, row=fila, padx=10, pady=10)
        else:
            self.tbl.place(x=pox, y=poy)
    
    def seleccionar(self):
        pass

    
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
            ventana()
  
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

#CLASE QUE GENERA UNA NUEVAS VENTANAS:

class ventana_base ():
    def __init__(self, geo="800x500", tl="SISTEMA DE CONTROL VEHICULAR", icon="./images/Micro.ico"):
        self.wn=tk.Toplevel()
        self.wn.geometry(geo)
        self.wn.title(tl)
        self.wn.iconbitmap(icon)
        self.wn.config(bg = "gray")
        self.wn.resizable(0,0)
    
    def mainloop(self):
        self.wn.mainloop()

    def return_tk(self):
        return self.wn

#CLASE QUE CREA UNA VENTANA PARA AGREFAR DATOS
class ventana_agregar_datos(ventana_base):
    def __init__(self, id_veh="", ruta="", chofer="", hora="", datos_anteriores=[], tablaexterna=None):
        self.vnt1=ventana_base("900x350", "INICIALIZADOR DE OPERACIONES")
        self.wn=self.vnt1.return_tk()
        self.id_veh=tk.StringVar(value=id_veh)
        self.ruta=tk.StringVar(value=ruta)
        self.chofer=tk.StringVar(value=chofer)
        self.hora=tk.StringVar(value=hora)
        self.lista_datos=[]
        self.tablaexterna=tablaexterna

        # CUERPO
        titulo(self.wn, 50, 20, "DATOS DE INGRESO").medida(300,30)

        titulo(self.wn, 50, 60, "VEHÍCULO").medida(100,30)
        cuadro_editor(self.wn, 200, 60, 150, 30, self.id_veh)
        titulo(self.wn, 50, 100, "RUTA").medida(100,30)
        cuadro_editor(self.wn, 200, 100, 150, 30, self.ruta)
        titulo(self.wn, 50, 140, "CHOFER").medida(100,30)
        cuadro_editor(self.wn, 200, 140, 150, 30, self.chofer)
        titulo(self.wn, 50, 180, "HORA").medida(100,30)
        cuadro_editor(self.wn, 200, 180, 150, 30, self.hora)

        # BOTONES
        boton(self.wn, 50, 230, "ENVIAR", "grey", self.agrega_vehiculo).medida(300)
        boton(self.wn, 50, 270, "FINALIZAR", "grey", self.verificar_acceso).medida(300)

        #TABLA
        titulo(self.wn, 450, 20, "VISTA PREVIA").medida(400,30)
        self.Tabla=table(self.wn, 4, ['ID_VEHICULO','RUTA','CHOFER','HORA'], False)
        if len(datos_anteriores) != 0:
            for valor in datos_anteriores:
                self.lista_datos.append(valor)
        self.Tabla.posicionar(pox=450, poy=60)
        boton(self.wn, 450, 305, "EDITAR VISTA PREVIA", "grey", self.ventana_editar_datos).medida(400)


    def agrega_vehiculo(self):
        linea = [self.id_veh.get(), self.ruta.get(), self.chofer.get(), self.hora.get()]
        lista_vacios = []
        for i in range(len(linea)):
            if linea[i] == "":
                lista_vacios.append(i)
    
        if len(lista_vacios) == 0:
            self.lista_datos.append(linea)
            self.Tabla.agregar_datos(linea)

            self.id_veh.set("")
            self.ruta.set("")
            self.chofer.set("")
            self.hora.set("")
        else:
            mb.showerror(message="Complete todos los campos", title="DATOS INCOMPLETOS")
            self.wn.destroy()
            ventana_agregar_datos(linea[0], linea[1], linea[2], linea[3], self.lista_datos, tablaexterna=self.tablaexterna)

    def retorna_datos(self):
        return self.lista_datos
    
    def verificar_acceso(self):
        
        def comprobar_contraseña():
            if conec.verificar_contraseña(self.vnt2.retorna_contra())==[[1]]:
                self.vnt2.return_tk().destroy()
                for dato in self.lista_datos:
                    self.tablaexterna.agregar_datos(dato)
                self.wn.destroy()
            elif self.vnt2.retorna_contra()=="":
                mb.showinfo(message="Ingrese un valor válido", title="SIN CONTRASEÑA")
                self.vnt2.return_tk().destroy()
                self.verificar_acceso()
            else:
                mb.showerror(message="Ingrese un valor correcto", title="CONTRASEÑA INCORRECTA")
                self.vnt2.return_tk().destroy()
                self.verificar_acceso()
                
        self.vnt2=ventana_verificar_acceso(command_verificacion=comprobar_contraseña)
        self.vnt2.mainloop()


    def ventana_editar_datos(self):
        pass

#CLASE QUE CREA UNA VENTANA PARA VERIFICAR ACCESO MEDIANTE UNA CONTRASEÑA
class ventana_verificar_acceso(ventana_base):
    def __init__(self, command_verificacion=None):
        self.vnt2=ventana_base("400x220", "COMPROBAR SU IDENTIDAD")
        self.wn=self.vnt2.return_tk()

        self.command_verificacion=command_verificacion
        
        self.contra=tk.StringVar()

        titulo(self.wn, 50, 20, "Ingrese una contraseña válida:").medida(300,30)
        cuadro_editor(self.wn, 50, 50, 300, 30, self.contra, contraseña=True)

        #BOTONES
        boton(self.wn, 50, 120, "INGRESAR", "grey", self.command_verificacion).medida(300)
        boton(self.wn, 50, 170, "CAMBIAR CONTRASEÑA", "grey").medida(300)
    
    def retorna_contra(self):
        return self.contra.get()
    


#CLASE QUE INICIALIAZ LA VENTANA PRINCIPAL

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
        boton(self.wn, 425, 310, "VER UNIDADES DETENIDAS", "dodger blue2").medida(200)
        boton(self.wn, 425, 345, "GENERAR REPORTE", "gold").medida(200)
        boton(self.wn, 425, 380, "EMITIR ALERTA VEHICULAR", "red").medida(200)
        boton(self.wn, 425, 415, "INICIAR OPERACIONES", "lawn green",self.pestaña_agregar_datos).medida(200) 
    
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
        self.Tabla.boton('VER DATOS COMPLETOS', 'grey')
        self.Tabla.boton('VER EN EL MAPA', 'grey', 1 , 3)
        self.Tabla.boton('TERMINAR LAS OPERACIONES', 'grey', 1 , 4)

        self.Tabla.posicionar()

    def mostrar_dato(self, dato):
        print(self.vnt.mostrar_dato())

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
    


# EJECUCUIÓN DE LA INTERFAZ
vn=ventana()


        

