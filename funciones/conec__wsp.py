import pywhatkit

class mensaje():
    def _init_(self):
        pass
    def conexion(self, numero, info):
        pywhatkit.sendwhatmsg_instantly(numero, info)

        