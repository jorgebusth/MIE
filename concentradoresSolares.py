import math
from openpyxl import load_workbook

wb = load_workbook('horno.xlsx')
sheet = wb['Hoja1']

Cg = float(input('Ingrese la concentración solar deseada: '))
b = float(input('Ingrese la longitud del absorbedor b [cm]: '))
largo = float(input('Ingrese el largo del absorbedor [cm]: '))
Ac = 2*b*largo
Tideal = 5800*math.pow(Cg/46000,0.25)
print('\nTemperatura ideal alcanzada:',Tideal-273.15,'ºC')



print('Area de captación:',Ac,'cm²')
print('Area del absorbedor',Ac/Cg,'cm²')
theta = math.asin(1/Cg)
#print(math.degrees(theta))

t = (math.pi/2) - theta
#print(math.degrees(t))

xmax =  (b * (1+math.sin(theta))) / (2*math.sin(theta))
print('x máxima=',xmax,'cm')


ymax = ( b * ( 1 + math.sin(theta) ) * math.cos(theta)  )/ ( 2 * math.pow(math.sin(theta),2) )
print('y máxima=',ymax,'cm')


# empiezan medidas de truncamiento

thetatr = float(input('Ingrese theta de truncamiento [rad]: '))
ttr = 1.5708-(3*thetatr)
print('Angulo de truncamiento:',math.degrees(ttr),'º')
j=-1
ttr= 0
g = -0.5



while(ttr<=1.5708-(3*thetatr)):
	
	xtr = ( b * ( 1 + math.sin(thetatr)) * math.cos(ttr) ) / (1 - math.sin(ttr-thetatr))
	ytr = ( b * ( 1 + math.sin(thetatr) ) * math.sin(ttr) ) / (1 - math.sin(ttr-thetatr))
	L = round(math.sqrt(math.pow(xtr,2)+math.pow(ytr,2)),2)

	ttr+=0.0088
	g+=0.5
	j=j+1
	# agregando datos a la hoja de cálculo
	row = (j,g,L)
	sheet.append(row)
	# guardando el libro
	wb.save('horno.xlsx')
	print('punto',j,'(',xtr,',',ytr,')')

