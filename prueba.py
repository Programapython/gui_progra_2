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
# import funciones.conec_arduino as conec
# import threading
# # print(conec.recibir_datos_tabla('2023-01-16'))
# print("hola mundo")
# hilo1=threading.Thread(target=conec.imprime)
# hilo1.start()
# print("chao mundo")


# import funciones.conec_arduino as arduino
# arduino.c_arduino()
# import funciones.funcionesGenerales as fng
# import funciones.conec_mysql as mysql
# from datetime import datetime
# # a=mysql.recibir_datos_tabla()[1][4]
# # b=datetime.strftime(a, '%Y/%m/%d')
# # print(b)
# fng.crear_doc()

# f = input('¿Finalizar o ruta?: ')

# cont = 0

# unidades = serial.Serial("COM16", 9600)
# time.sleep(0.5)

# while True:
   
#     if f == 'ruta':
#         n = int(input("ingrese la ruta : "))
#         if n == 1:
#             cont +=1
#             print(cont)
#             while (cont <=1):
#                 unidades.write('1'.encode())
#                 time.sleep(0.1)

#         if n == 2:

#             cont +=1
#             print(cont)
#         while (cont <=1):
#             unidades.write('2'.encode())
#             time.sleep(0.1)

#     if f == 'finalizar':
#         cont +=1
#         print(cont)
#         while (cont <=1):
#             unidades.write('0'.encode())
#             time.sleep(0.1)
# a=serial.Serial("COM16",9600)
# time.sleep(0.5)
# i=1
# for i in range(2):
#     a.write(str(i).encode())
#     if i == 1:
#         pass
#     input("djashdj")
# a=serial.Serial("COM16",9600)
# time.sleep(2)
# for i in range(10):
#     time.sleep(2)
#     a.write(f"12:{i}".encode("ascii"))

