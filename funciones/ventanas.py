import tkinter as tk

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

#CLASE QUE GENERA CUADROS PARA INGRESAR DATOS
class dato():
    def __init__(self, wn, pox, poy, informacion, base=50, altura=30, color="grey", fuente = ("Arial", 10)):
        self.dt=tk.Label(wn, text=informacion, fg="black", bg= color, font = fuente, justify= "left")
        self.dt.place(x=pox, y=poy, width=base, height=altura)

#CLASE QUE GENERA UN BOTON
class boton():
    def __init__(self, wn, texto = 'texto predefinido', color='white', cmd=None):
        self.bt= tk.Button(wn, text = texto, bg = color, command=cmd, font = ("Arial", 9))

    def medida_posicion(self, base=10, pox=0, poy=0):
        self.bt.place(width=base, height=30, x=pox, y=poy)

    def grid(self,pox, poy):
        self.bt.grid(column=pox, row=poy, padx=10, pady=10)


#CLASE QUE CONTIENE A VENTANAS ADICIONALES A LA APLICACIÓN
class vnt():
    def __init__(self):
        pass
    def acerca_de(self):
        self.vnt = ventana_base("400x100", "ACERCA DE ...")
        self.wn = self.vnt.return_tk()
        self.linea = dato(self.wn, 10, 10, "ESTE PROGRAMA HA SIDO CREADO COMO PARTE DE UN\nPROYECTO PARA LA ASIGNATURA DE PROGRAMACIÓN II", 380, 40, fuente = ("Arial", 10))
        self.boton1 = boton(self.wn, "VER REPOSITORIO (GITHUB)", "grey", None).medida_posicion(185, 10, 60)
        self.boton2 = boton(self.wn, "DESCARGAR INSTALADOR", "grey", None).medida_posicion(185, 205, 60)
        self.wn.mainloop()


