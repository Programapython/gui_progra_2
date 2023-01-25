from tkinter import messagebox
import pylatex as ptx
import webbrowser as wb
import fpdf
import shutil
import time
import funciones.conec_mysql as conec

class convert():
    def __init__(self, arg= None):
        self.arg = arg
        self.strORlist = arg

    # CONVERTIR LISTA DE LISTAS DEL MODO [['8', '8'], ['9', '9']] EN UN STRING
    def list_string(self, list = None):
        if list != None:
            self.strORlist = list
        elif list == None:
            print("Faltan argumentos")
            pass
            
        new_string = ""

        for i in self.strORlist:
            new_string += ",".join(i)
            new_string += "\n"  

        return new_string

    # CONVERTIR UN STRING EN UNA LISTA DE LISTAS DEL MODO [['8', '8'], ['9', '9']]
    def string_list(self, string = None):

        if string != None:
            self.strORlist = string
        elif string == None:
            print("Faltan argumentos")
            pass

        new_list_list = []
        for i in self.strORlist:
            string=i[:-1]
            new_list=string.split(",")
            new_list_list.append(new_list)
        return new_list_list


"""##############################################################################################################"""
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
"""##############################################################################################################"""

# ESCRIBIR/LEER DOCUMENTO
class doc(convert):
    # Doc HEREDA LOS MÉTODOS DE LA CLASE CONVERT 
    def __init__(self, doc = "./documentos/data.txt"):
        self.doc = doc
    
    def operacion(self, opcion, informacion = None):

        self.strORlist = informacion 

        if opcion == "soloE":
            modo = "a"
        elif opcion == "E" or opcion == "B":
            modo = "w"
        elif opcion == "L":
            modo = "r"
        elif opcion == "LE":
            modo = "r"
        
        with open(self.doc, modo) as file:
            if opcion == "soloE" or opcion == "E":
                self.string = self.list_string(informacion)
                file.write(self.string)
            elif opcion == "L":
                L=self.string_list(file.readlines())
                del L[0]
                return L
            elif opcion == "LE":
                L=self.string_list(file.readlines())
                return L
            elif opcion == "B":
                file.write("")


"""##############################################################################################################"""
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
"""##############################################################################################################"""
#FUNCIONES VARIADAS QUE MODIFICAN CARACTERISTICAS Y DATOS DE LA APLICACIÓN

def cambiar_doc2(encabezado, nuevo_valor):
    contenido_data=doc("./documentos/data2.txt").operacion("LE")
    for encabezado_dato in contenido_data:
        if encabezado_dato[0] == encabezado:
            encabezado_dato[1] = nuevo_valor
            break
    doc("./documentos/data2.txt").operacion("E",contenido_data)

def finalizar_op():
    #ENVIA LOS DATOS CONTENIDOS EN EL ARCHIVO DATA A LA BASE DE DATOS
    #conec.enviar_datos_tabla()
    # BORRA LOS DATOS DE DATA PARA QUE MUESTRE SOLO ENCABEZADOS
    doc().operacion("E",
        [['ID_SALIDA','ID_VEHICULO','RUTA','CHOFER','HORA_SALIDA','DIA_SALIDA','MARCA_1','VEL_1','MARCA_2','VEL_2','MARCA_3','VEL_3','MARCA_LLEGADA']])
    # COLOCAR EL CONTADOR DE LOS MAPAS EN CERO
    cambiar_doc2("numero_mapas","0")
    # COLOCAR EL CONTADOR DE NUMERO DE SALIDAS EN CERO
    cambiar_doc2("numero_salidas","0")

def buscar_doc2(dato_buscado=None):
    datos_encabezados=doc("./documentos/data2.txt").operacion("LE")
    for encabezado_dato in datos_encabezados:
        if encabezado_dato[0] == dato_buscado:
            return encabezado_dato[1]

def agregar_nueva_salida(data_ingresada):
    n_salida=buscar_doc2("numero_salidas")
    nuevas_salidas=data_ingresada
    for data in nuevas_salidas:
        n_salida=int(n_salida)+1
        data.insert(0,str(n_salida))
    
    cambiar_doc2("numero_salidas",str(n_salida))
    doc().operacion("soloE",nuevas_salidas)

def modificar_salida(id_salida):
    datos_salida=doc().operacion("LE")
    for salida in datos_salida:
        if salida[0] == id_salida:
            salida.append(time.strftime('%H:%M:%S'))
            doc().operacion("E",datos_salida)
            break

"""##############################################################################################################"""
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
"""##############################################################################################################"""

#ABRIR DIRECCIONES WEB

# lista de enlaces
repositorio_git_proyecto = "https://github.com/Programapython/gui_progra_2"
instaladores = "https://drive.google.com/drive/folders/14vLAJIizDJtl1uRlQGc7pIsXCnJ9yMzS?usp=sharing"

class abre():
    def __init__(self, opcion, ventana):
        
        if opcion == "repo":
            wb.open(repositorio_git_proyecto)
        elif opcion == "insta":
            wb.open(instaladores)

        #CIERRA LA VENTANA DE TKINTER QUE NOS REDIRECCIONA AL ENLACE
        if ventana != None:
            ventana.destroy()

# ------------------------------------------------------------------------------------------------------------------
"""##############################################################################################################"""
class crear_doc():
    def __init__(self, fecha_solicitada, *vehiculos_buscados):
        pdf=fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)
        fecha=time.strftime('%Y-%m-%d')
        pdf.cell(190,10,txt="INFORME",border=True, ln=1, align="C")
        pdf.cell(200,10, txt=f"Fecha de solicitud: {fecha}",ln=1, align="left")
        pdf.cell(200,10, txt=f"Fecha solicitada: {fecha_solicitada}", ln=1, align="left")
        pdf.cell(200,10, txt=f"Unidad (es) buscadas: {vehiculos_buscados}", ln=6, align="left")
        pdf.output(dest='F',name=f"./documentos/informes/{fecha}_{vehiculos_buscados}.pdf")
        shutil.copy(f"./documentos/informes/{fecha}_{vehiculos_buscados}.pdf", buscar_doc2("direccion_informe"))


# ------------------------------------------------------------------------------------------------------------------
"""##############################################################################################################"""