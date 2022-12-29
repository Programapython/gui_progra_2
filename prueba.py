import tkinter as tk
from tkinter import messagebox, ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Vista de árbol en Tkinter")
        self.treeview = ttk.Treeview(self)
        self.my_iid = "id_unico"
        self.treeview.insert("", tk.END, text="Elemento 1", iid=self.my_iid)
        self.treeview.pack()
        self.button = ttk.Button(text="Mostrar información",
                                 command=self.show_info)
        self.button.pack(after=self.treeview)
        self.pack()
    
    def show_info(self):
        # Obtener el texto del Elemento 1.
        text = self.treeview.item(self.my_iid, option="text")
        # Mostrarlo en un cuadro de diálogo.
        messagebox.showinfo(title="Información", message=text)
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()