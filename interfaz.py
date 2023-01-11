from tkinter import Tk, Label, Button, Entry, ttk
import time

#Ventana
ventana = Tk()
ventana.geometry("800x500")
ventana.title("SISTEMA DE CONTROL VEHICULAR")
ventana.iconbitmap("./imagenes/Micro.ico")
ventana.config(bg = "gray")
ventana.resizable(0,0)

#Frame
style = ttk.Style()
style.configure("BW.TFrame", background="black")

frame=ttk.Frame(ventana, style="BW.TFrame")
frame.config(width=360, height=400)
frame.place(x=40, y=120)

#Titulo
titulo1 = Label(ventana, text = "SOFTWARE DE RASTREO Y CONTROL",fg = "cyan", bg = "black")
titulo1.place(x = 250, y = 20, width = 250, height = 40)

titulo2 = Label(ventana, text = "DATOS GENERALES:",fg = "cyan", bg = "black")
titulo2.place(x = 400, y = 80, width = 150, height = 30)

titulo3 = Label(ventana, text = "VEHÍCULOS EN CIRCULACIÓN",fg = "cyan", bg = "black")
titulo3.place(x = 425, y = 135, width = 200, height = 30)
texto1 = Entry(ventana, bg = "cyan")
texto1.place(x = 630, y = 135, width = 50, height = 30)

titulo4 = Label(ventana, text = "VEHÍCULOS NO CIRCULACIÓN",fg = "cyan", bg = "black")
titulo4.place(x = 425, y = 170, width = 200, height = 30)
texto2 = Entry(ventana, bg = "cyan")
texto2.place(x = 630, y = 170, width = 50, height = 30)

titulo5 = Label(ventana, text = "VEHÍCULOS FUERA DE SERVICIO",fg = "cyan", bg = "black")
titulo5.place(x = 425, y = 205, width = 200, height = 30)
texto3 = Entry(ventana, bg = "cyan")
texto3.place(x = 630, y = 205, width = 50, height = 30)

titulo6 = Label(ventana, text = "VEHÍCULOS TOTALES",fg = "cyan", bg = "black")
titulo6.place(x = 425, y = 240, width = 200, height = 30)
texto4 = Entry(ventana, bg = "cyan")
texto4.place(x = 630, y = 240, width = 50, height = 30)

titulo7 = Label(ventana, text = "N° UNIDADES DETENIDAS",fg = "cyan", bg = "black")
titulo7.place(x = 425, y = 275, width = 200, height = 30)
texto5 = Entry(ventana, bg = "cyan")
texto5.place(x = 630, y = 275, width = 50, height = 30)

titulo8 = Label(ventana, text = "FECHA",fg = "cyan", bg = "black")
titulo8.place(x = 425, y = 460, width = 50, height = 30)
fecha = Label(ventana, text = time.strftime('%d/%m/%Y'), font = ("Tahoma", 15), fg = "black", bg = "cyan")
fecha.place(x = 480, y = 460, width = 120, height = 30)

titulo9 = Label(ventana, text = "HORA",fg = "cyan", bg = "black")
titulo9.place(x = 620, y = 460, width = 50, height = 30)
hora = Label(ventana, text = time.strftime('%H:%M:%S'), font = ("Tahoma", 15), fg = "black", bg = "cyan")
hora.place(x = 675, y = 460, width = 100, height = 30)

def reloj():
    hora_actual = time.strftime('%H:%M:%S') 
    if hora["text"] != hora_actual:
        hora["text"] = hora_actual
    ventana.after(1000, reloj)

#Botones
boton1 = Button(ventana, text = "VER UNIDADES DETENIDAS", bg = "dodger blue2")
boton1.place(x = 425, y = 310, width = 200, height = 30)

boton2 = Button(ventana, text = "GENERAR REPORTE", bg = "gold")
boton2.place(x = 425, y = 345, width = 150, height = 30)

boton3 = Button(ventana, text = "EMITIR ALERTA VEHICULAR", bg = "red")
boton3.place(x = 425, y = 380, width = 200, height = 30)

boton4 = Button(ventana, text = "INICIAR OPERACIONES", bg = "lawn green")
boton4.place(x = 425, y = 415, width = 150, height = 30)


#Tabla
tbl=ttk.Treeview(frame, columns=('col1','col2'))
tbl.column("#0", width=100, anchor="center")
tbl.column("col1", width=100, anchor="center")
tbl.column("col2", width=100, anchor="center")

tbl.heading("#0", text="ID_VEHICULO", anchor="center")
tbl.heading("col1", text="RUTA", anchor="center")
tbl.heading("col2", text="POSICIÓN", anchor="center")

id1=tbl.insert("","end", text="1", values=('A', 'PARADERO 1'))
id1=tbl.insert("","end", text="2", values=('B', 'PARADERO 2'))
id1=tbl.insert("","end", text="3", values=('C', 'PARADERO 3'))
id1=tbl.insert("","end", text="4", values=('B', 'PARADERO 4'))
id1=tbl.insert("","end", text="5", values=('C', 'PARADERO 5'))
id1=tbl.insert("","end", text="6", values=('A', 'PARADERO 6'))
id1=tbl.insert("","end", text="7", values=('B', 'PARADERO 7'))
id1=tbl.insert("","end", text="8", values=('C', 'PARADERO 8'))
id1=tbl.insert("","end", text="9", values=('B', 'PARADERO 9'))
id1=tbl.insert("","end", text="10", values=('C', 'PARADERO 10'))
id1=tbl.insert("","end", text="1", values=('A', 'PARADERO 1'))
id1=tbl.insert("","end", text="2", values=('B', 'PARADERO 2'))
id1=tbl.insert("","end", text="3", values=('C', 'PARADERO 3'))
id1=tbl.insert("","end", text="4", values=('B', 'PARADERO 4'))
id1=tbl.insert("","end", text="5", values=('C', 'PARADERO 5'))

tbl.grid(column=1, row=1, padx=10, pady=10) 

#Boton tabla
boton5 = Button(frame, text = "VER DATOS COMPLETOS", bg = "lawn green")
boton5.grid(column=1, row=3, padx=5, pady=10)



reloj()
ventana.mainloop()