import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import funciones.funcionesGenerales as fng
import funciones.conec_mysql as conec
import time


'''
ESTE MÓDULO CONTIENE LAS CLASES QUE CREAN VENTANAS INDEPENDIENTES Y ELEMENTOS PARA CONSTRUIRLAS
'''


#CLASE QUE GENERA UN BOTÓN
class boton():
    def __init__(self, wn, texto = 'texto predefinido', color='white', cmd=None):
        self.bt= tk.Button(wn, text = texto, bg = color, command=cmd)

    def medida_posicion(self, base=10, pox=0, poy=0):
        self.bt.place(width=base, height=30, x=pox, y=poy)

    def grid(self,pox, poy):
        self.bt.grid(column=pox, row=poy, padx=10, pady=10)


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

    def posicionar(self, columna=1, fila=1, pox=0, poy=0):
        if self.opcion == True:
            self.tbl.grid(column=columna, row=fila, padx=10, pady=10)
        else:
            self.tbl.place(x=pox, y=poy)
    
    def seleccionar(self):
        pass

    def tkframe(self):
        return self.sp

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

    def titulos2(self, posicion, nombre, nombre_comando = lambda: print("No exite un comando"), atajo=""):
        #crea un elemento del submenú, este se obtiene del parámetro normbre
        #n indica la posición del submenú al cual se le van a añadir los elementos
        
        #Agregar el nuevo submenpu y el comando correspondiente
        self.t1[posicion-1].add_command(label=nombre, accelerator=atajo, command=nombre_comando) 
        
        if atajo =='Ctrl+N':
            self.ventana.bind_all("<Control-n>", nombre_comando)
    
    def separador(self, posicion):
        self.t1[posicion-1].add_separator()

#CLASE QUE GENERA UNA VENTANA BÁSICA TOPLEVEL
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

#CLASE QUE CREA UNA VENTANA PARA AGREGAR DATOS
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
        boton(self.wn, "ENVIAR", "grey", self.agrega_vehiculo).medida_posicion(300, 50, 230)
        boton(self.wn, "FINALIZAR", "grey", self.verificar_acceso).medida_posicion(300, 50, 270)

        #TABLA
        titulo(self.wn, 450, 20, "VISTA PREVIA").medida(400,30)
        self.Tabla=table(self.wn, 4, ['ID_VEHICULO','RUTA','CHOFER','HORA'], False)
        if len(datos_anteriores) != 0:
            for valor in datos_anteriores:
                self.lista_datos.append(valor)
        self.Tabla.posicionar(pox=450, poy=60)
        boton(self.wn, "EDITAR VISTA PREVIA", "grey", self.ventana_editar_datos).medida_posicion(400, 450, 305)


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
                fng.doc().operacion("E",self.lista_datos)
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
        boton(self.wn, "INGRESAR", "grey", self.command_verificacion).medida_posicion(300, 50, 120,)
        boton(self.wn, "CAMBIAR CONTRASEÑA", "grey").medida_posicion(300, 50, 170)
    
    def retorna_contra(self):
        return self.contra.get()


#CLASE QUE CONTIENE A VENTANAS ADICIONALES E INDEPENDIENTES DE LA APLICACIÓN
class vnt():
    def __init__(self):
        pass
    def acerca_de(self):
        self.vnt = ventana_base("400x100", "ACERCA DE ...")
        self.wn = self.vnt.return_tk()
        self.linea = dato(self.wn, 10, 10, "ESTE PROGRAMA HA SIDO CREADO COMO PARTE DE UN\nPROYECTO PARA LA ASIGNATURA DE PROGRAMACIÓN II", 380, 40, fuente = ("Arial", 10))
        self.boton1 = boton(self.wn, "VER REPOSITORIO (GITHUB)", "grey", lambda: fng.abre("repo", self.wn)).medida_posicion(185, 10, 60)
        self.boton2 = boton(self.wn, "DESCARGAR PROGRAMA", "grey", lambda: fng.abre("insta", self.wn)).medida_posicion(185, 205, 60)
        self.wn.mainloop()


'''
CLASES DESECHADAS/INUTILIZADAS
'''

# #CLASE QUE GENERA UN FRAME EN LA VENTANA
# class espacio():
#     def __init__(self, wn, color, pox, poy, base=10, altura=10):
#         self.frame=tk.Frame(wn, bg=color)
#         self.frame.config(width=base, height=altura)
#         self.frame.place(x=pox, y=poy)
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# ----------------------------------------------------
# #GENERA UNA SUBVENTANA
# class subventana():
#     def __init__(self, wn, color, pox, poy, base=10, altura=10):
#         self.subv=wn.Toplevel(wn, bg=color)
#         self.frame.config(width=base, height=altura)
#         self.frame.place(x=pox, y=poy)