'''Este programa sirve para sensar la temperatura de un LM35 junto con el MCP3008
y guardarla en una hoja de cálculo para su análisis posterior'''
import gpiozero
from gpiozero import MCP3008
import time
from time import sleep
from openpyxl import load_workbook
import datetime
from datetime import date

#wb = load_workbook('horno.xlsx')  #abre hoja de cálculo
#hoja = wb['Sheet1']    # selecciona la hoja en la que sescribirán los datos

lectura = MCP3008(0)
lectura1 = MCP3008(1)
lectura2 = MCP3008(2)
while True:
    hoy = date.today()
    now = datetime.datetime.now().time()
    temp1 = round(lectura.value * 100 , 2)
    temp2 = round(lectura1.value * 100 * 3.3 , 2)
    temp3 = round(lectura1.value * 100 * 3.3 , 2)
    #row = (hoy,now,temp1,temp2,temp3)
    #hoja.append(row)
    #wb.save('horno.xlsx')
    print(hoy,now,temp1,temp2,temp3)
    sleep(2)