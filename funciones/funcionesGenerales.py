import pylatex as ptx
# from pylatex import Document, section, Subsection, 

#FUNCION QUE CREA UN DOCUMENTO PDF

# nuevo_documento=Document()
# nuevo_documento.generate_pdf()

# from pylatex import Document, Section, Subsection
# from pylatex.utils import italic, NoEscape


# def fill_document(doc):
#     """Add a section, a subsection and some text to the document.

#     :param doc: the document
#     :type doc: :class:`pylatex.document.Document` instance
#     """
#     with doc.create(Section('A section')):
#         doc.append('Some regular text and some ')
#         doc.append(italic('italic text. '))

#         with doc.create(Subsection('A subsection')):
#             doc.append('Also some crazy characters: $&#{}')


# if __name__ == '__main__':
#     # Basic document
#     doc = Document('basic')
#     fill_document(doc)

#     doc.generate_pdf(filepath="hola",clean_tex=True, compiler="pdflatex", clean=True)

# ------------------------------------------------------------------------------------------------------------------
"""##############################################################################################################"""

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

# ESCRIBIR DOCUMENTO
class doc(convert):
    # Doc HEREDA LOS MÉTODOS DE LA CLASE CONVERT 
    def operacion(self, opcion, informacion = None):

        self.strORlist = informacion 

        if opcion == "soloE":
            modo = "a"
        elif opcion == "E" or opcion == "B":
            modo = "w"
        elif opcion == "L":
            modo = "r"
        
        with open("./documentos/data.txt", modo) as file:
            if opcion == "soloE" or opcion == "E":
                self.string = self.list_string(informacion)
                file.write(self.string)
            elif opcion == "L":
                return self.string_list(file.readlines())
            elif opcion == "B":
                file.write("")

