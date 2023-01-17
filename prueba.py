# import pyautogui as pa
# import webbrowser as wb
# import time
# # a=wb.get('lynx')
# # a.open_new("http://meet.google.com/uff-ysob-kgp")
# time.sleep(5)
# print(pa.position())
# time.sleep(5)
# print(pa.position())
# time.sleep(5)
# print(pa.position())
# time.sleep(5)
# print(pa.position())
# from tkinter import messagebox
# import pandas as pd
# import time

# # confirmacion=messagebox.askyesnocancel(title="FINALIZACIÓN DE LAS OPERACIONES", 
# #                 message="Esta seguro que desea terminar las operaciones")
# # if confirmacion == True:
# #     print("me estoy ejecutando")
# vehiculos = pd.read_csv('./documentos/data.txt')
# vehiculos.query(f"RUTA == 'A'")
# horas_salida = vehiculos['HORA_SALIDA'].to_list()
# marcas1 = vehiculos['MARCA_1'].to_list()
# marcas2 = vehiculos['MARCA_2'].to_list()
# marcas3 = vehiculos['MARCA_3'].to_list()

# for hora_salida, marca1, marca2, marca3 in zip(horas_salida, marcas1, marcas2, marcas3):
#     a=type(True)
#     # if hora_salida == time.strftime('%H:%M:%S'):
#     #     print('inicio')
#     # else:
#     #     print('no inicio')
#     if a==bool:
#         print("cadena")
import funciones.conec_mysql as conec
print(conec.recibir_datos_tabla('2023-01-16'))