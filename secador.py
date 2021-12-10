
''' Este programa sirve pára sensar la temperatura de varios LM35 junto 
	con el MCP3008 y guardar los datos en una hoja de calculo para 
	su analisis posterior'''

# No olvidar instalar las bibliotecas.

import sys
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from openpyxl import load_workbook
import datetime
from datetime import date

wb = load_workbook('secador.xlsx') # Abre la hoja de calculo, debe estar en el mismo directorio o especificar la ruta.
hoja = wb['Sheet1'] # Selecciona la hoja en la que se guardaran los datos.
VREF = 4.88	# Se asigna el voltaje de referencia que es igual al de alimentacion del MCP3008

'''	Se puede usar software SPI o hardware SPI tambien. Para software SPI se
	usara los pines regulares GPIO. Para hardware SPI se usa los pines SPI
	en la Raspberry Pi. Ajustar las siguientes varibles para cualquiera 
	para HW o SW para hardware SPI y Software SPI respectivamente '''
SPI_TYPE = 'HW'
retardo = 60 # Retardo en segundos

# Configuracion software SPI
CLK = 18	# Ajusta el pin serial Reloj
MISO = 23	# Ajusta el pin Maestro Entrada Esclavo Salida
MOSI = 24	# Ajusta el pin Maestro Salida Esclavo Entrada
CS = 25		# Ajusta la Seleccion de Esclavo

# Configuraci{on hardware SPI
HW_SPI_PORT = 0 # Ajusta el puerto SPI. Raspberry Pi tiene dos puertos
HW_SPI_DEV = 0  # Ajusta el dispositivo SPI

# Instancia la clase mcp desde el modulo Adafruit_MCP3008 y lo ajusta en 'mcp'
if(SPI_TYPE == 'HW'):
	# Usa esto para hardware SPI
	mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(HW_SPI_PORT,HW_SPI_DEV))
elif(SPI_TYPE == 'SW'):
	# Usa esto para software SPI
	mcp = Adafruit_MCP3008.MCP3008(clk = CLK,cs = CS, miso = MISO, mosi = MOSI)

# Revisa para ver si tenemos entradas desde la linea de comando. Fianza si no tenemos
if (len(sys.argv) <= 1):
	print ("Uso: secador.py 0")
	sys.exit(1)
else:
	# Asigno los puertos a leer
	analogPort0 = 0
	analogPort1 = 1
	analogPort2 = 2
	analogPort3 = 3

try:
	while True:

		hoy = date.today()	# Asigno la fecha a hoy
		ahora = datetime.datetime.now().time() # Asigno la hora a ahora
		valor0 = mcp.read_adc(analogPort0)	# Lee el valor del pin 0 del MCP3008
		valor1 = mcp.read_adc(analogPort1)	# Lee el valor del pin 1 del MCP3008
		#valor2 = mcp.read_adc(analogPort2)	# Lee el valor del pin2 del MCP3008
		#valor3 = mcp.read_adc(analogPort3)	# Lee el valor del pin 3
		# Por regla de tres hago la conversion para grados Celcius
		valor0 = ((valor0 * VREF) / 1023) * 100
		valor1 = ((valor1 * VREF) / 1023) * 100
		#valor2 = ((valor2 * VREF) / 1023) * 100
		#valor3 = ((valor3 * VREF) / 1023) * 100
		# Se guardan los datos obtenidos y se muestran en pantalla
		fila = (hoy,ahora,valor0,valor1)	# Se forma la fila para la hoja de calculo con las variables seleccionadas
		hoja.append(fila)	# Se agrega los datos de la fila formada a la hoja seleccionada
		wb.save('secador.xlsx')	# Se guarda el archvo xlsx
		print (valor0,valor1)	# Se muestra en pantalla los datos ingresados a la hoja


		# Pausa por el retraso
		sleep(retardo)

except KeyboardInterrupt:
	wb.save('secador.xlsx')
	sys.exit()
